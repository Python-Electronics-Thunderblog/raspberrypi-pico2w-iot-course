from machine import ADC, Pin
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
# Grove シールドの A0 コネクタ = GP26
LIGHT_SENSOR_PIN = 26

# ── ADC初期化 ────────────────────────────────────────────────────────
# ADC(Pin(26)) で GP26 をアナログ入力として設定する
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 0.5  # 0.5秒ごとに読み取る

print("照度センサー 読み取り開始")
print("センサーを手で遮ったり、光を当てて値の変化を確認してください")

# ── メインループ ─────────────────────────────────────────────────────
while True:
    # read_u16() は 0〜65535 の整数を返す
    # 0 = 最も暗い（電圧 0V）、65535 = 最も明るい（電圧 3.3V）
    adc_value = light_sensor.read_u16()

    # 0〜65535 を 0〜100% に換算（表示用）
    percent = round(adc_value / 65535 * 100, 1)

    print(f"ADC: {adc_value:5d}  照度: {percent:5.1f}%")
    time.sleep(INTERVAL_SEC)
