from machine import ADC, Pin, PWM
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
LIGHT_SENSOR_PIN = 26   # Grove A0 コネクタ
LED_PIN          = 16   # Grove D16 コネクタ

# ── キャリブレーション値（実測で調整） ───────────────────────────────
ADC_MIN = 1000     # 最も暗い時の実測 ADC値（完全遮光）
ADC_MAX = 27000   # 最も明るい時の実測 ADC値（撮影レイアウト＝OBS分割・カメラON時）

# ── PWM設定 ─────────────────────────────────────────────────────────
PWM_FREQ = 1000   # 1kHz：人の目にちらつきが見えない周波数

# ── スムージング係数 ─────────────────────────────────────────────────
# 急な変化を抑えて「じわっと」変化させる（0.0〜1.0）
# 小さいほどゆっくり、大きいほど素早く反応する
SMOOTH_ALPHA = 0.1

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 0.05  # 50ms（滑らかに見せるため短め）

# ── 初期化 ───────────────────────────────────────────────────────────
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))
led = PWM(Pin(LED_PIN))
led.freq(PWM_FREQ)
led.duty_u16(0)  # 起動時は消灯

# スムージング用（現在のduty値を float で保持）
current_duty = 0.0

print("PWM 調光プログラム 開始")
print(f"キャリブレーション: ADC {ADC_MIN}〜{ADC_MAX} → LED 最大〜最小")
print("手でセンサーを遮ると LED がじわっと明るくなります")


def remap(value: int, in_min: int, in_max: int, out_min: int, out_max: int) -> float:
    """
    value を in_min〜in_max の範囲から out_min〜out_max の範囲に線形変換する。
    範囲外の値はクランプ（切り捨て）する。

    例: remap(30000, 15000, 45000, 0, 65535) → 32767.5
    """
    # 入力範囲でクランプ（範囲外の値を端点に合わせる）
    value = max(in_min, min(in_max, value))
    # 線形補間
    ratio = (value - in_min) / (in_max - in_min)
    return out_min + ratio * (out_max - out_min)


# ── メインループ ─────────────────────────────────────────────────────
while True:
    # センサー値を読み取る（明るいほど大きい値）
    adc_value = light_sensor.read_u16()

    # ADC値を 0〜65535 にリマップしてから反転
    #   明るい(ADC大) → リマップ後も大 → 反転で小 → LED 暗い
    #   暗い(ADC小)   → リマップ後も小 → 反転で大 → LED 明るい
    mapped  = remap(adc_value, ADC_MIN, ADC_MAX, 0, 65535)
    target_duty = 65535 - mapped

    # スムージング: target に向けて少しずつ近づける
    current_duty += SMOOTH_ALPHA * (target_duty - current_duty)

    # duty_u16() は整数のみ受け付ける
    led.duty_u16(int(current_duty))

    percent = round(adc_value / 65535 * 100, 1)
    print(f"ADC: {adc_value:5d}  照度: {percent:5.1f}%  duty: {int(current_duty):5d}")
    time.sleep(INTERVAL_SEC)
