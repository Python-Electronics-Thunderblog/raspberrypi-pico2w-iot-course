from machine import I2C, Pin
import dht
import time

# grove_lcd.py は、先に Thonny で Pico 本体へ保存しておく
from grove_lcd import GroveLCD

# ── I2C 設定 ─────────────────────────────────────────────────────────
I2C_ID = 1           # Grove I2C1 コネクタ
SCL_PIN = 7
SDA_PIN = 6
I2C_FREQ = 400_000

# ── ピン設定 ─────────────────────────────────────────────────────────
DHT11_PIN = 16       # Grove D16 コネクタ（第5回と同じ）

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 2     # DHT11 は「1秒に1回まで」

# ── 初期化 ───────────────────────────────────────────────────────────
i2c = I2C(I2C_ID, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=I2C_FREQ)
lcd = GroveLCD(i2c)
sensor = dht.DHT11(Pin(DHT11_PIN))

print("DHT11 の温湿度を LCD に表示 開始")
print("-" * 40)

# ── メインループ ─────────────────────────────────────────────────────
# 第5回の 03_dht11_logger.py の print() を lcd.write_line() に置き換えただけ
# 表示先が Shell から LCD に変わったので、PC につながなくても値が見える
while True:
    try:
        sensor.measure()
        # 桁が変わっても（例: 湿度 100 → 99）前の文字が残らないよう write_line() を使う
        # 「℃」は LCD で文字化けするので、英字の C で表す
        lcd.write_line(0, f"Temp: {sensor.temperature()} C")
        lcd.write_line(1, f"Humi: {sensor.humidity()} %")
    except OSError as e:
        # 読み取りに失敗したら、LCD に「Error」、Shell に理由を出す
        # ※ LCD のケーブルを抜いたときは、ここで LCD へ書こうとして止まる
        lcd.write_line(0, "Error")
        lcd.write_line(1, "")
        print("センサーの読み取りに失敗しました:", e)
    time.sleep(INTERVAL_SEC)
