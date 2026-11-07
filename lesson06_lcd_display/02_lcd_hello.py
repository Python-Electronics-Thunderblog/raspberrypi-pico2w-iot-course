from machine import I2C, Pin
import time

# grove_lcd.py は、先に Thonny で Pico 本体へ保存しておく
# （保存し忘れると ImportError: no module named 'grove_lcd' になる）
from grove_lcd import GroveLCD

# ── I2C 設定 ─────────────────────────────────────────────────────────
I2C_ID = 1           # Grove I2C1 コネクタ
SCL_PIN = 7
SDA_PIN = 6
I2C_FREQ = 400_000

# ── 表示の設定 ───────────────────────────────────────────────────────
COUNT_FROM = 10      # 2行目に 10 → 1 と数えて表示する
INTERVAL_SEC = 1     # 1秒ごとに数を変える

# ── 初期化 ───────────────────────────────────────────────────────────
i2c = I2C(I2C_ID, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=I2C_FREQ)
lcd = GroveLCD(i2c)   # 2行表示・表示ON・画面を消す、までをまとめて行う

print("LCD 表示テスト 開始")

# ── 1行目: 文字を出す ────────────────────────────────────────────────
lcd.write_line(0, "Hello, Pico 2W!")

# ── 2行目: 数字を出す ────────────────────────────────────────────────
# 10 → 9 で桁が減っても、write_line() は16文字ぶん空白で埋めて上書きするので
# 「90」のように前の文字が残らない
for count in range(COUNT_FROM, 0, -1):
    lcd.write_line(1, f"Count: {count}")
    print(f"Count: {count}")
    time.sleep(INTERVAL_SEC)

# ── 画面を消す ───────────────────────────────────────────────────────
lcd.clear()
print("画面を消しました")
