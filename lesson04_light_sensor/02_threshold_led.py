from machine import ADC, Pin
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
LIGHT_SENSOR_PIN = 26   # Grove A0 コネクタ
LED_PIN          = 16   # Grove D16 コネクタ

# ── しきい値 ─────────────────────────────────────────────────────────
# この値より ADC値が小さい（暗い）と LED が点灯する
# 撮影時実測: 通常時　　 ≈ 30000
# 撮影時実測：手をかざす ≈ 10000
# → 中間の 20000 をしきい値に設定
THRESHOLD = 20000

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 0.1  # 0.1秒ごとに確認（素早く反応させる）

# ── LED状態の定義（可読性のため定数化） ─────────────────────────────
LED_ON  = 1
LED_OFF = 0

# ── 初期化 ───────────────────────────────────────────────────────────
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))
led          = Pin(LED_PIN, Pin.OUT)

led.value(LED_OFF)  # 起動時はLED消灯

print("しきい値判定プログラム 開始")
print(f"THRESHOLD = {THRESHOLD}  （暗い → LED点灯）")
print("-" * 40)

# ── メインループ ─────────────────────────────────────────────────────
while True:
    adc_value = light_sensor.read_u16()

    if adc_value < THRESHOLD:
        # 暗い → LED 点灯
        led.value(LED_ON)
        status = "暗い  → LED ON"
    else:
        # 明るい → LED 消灯
        led.value(LED_OFF)
        status = "明るい → LED OFF"

    print(f"ADC: {adc_value:5d}  {status}")
    time.sleep(INTERVAL_SEC)
