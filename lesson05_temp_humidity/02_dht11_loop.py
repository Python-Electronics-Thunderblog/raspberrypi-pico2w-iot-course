from machine import Pin
import dht
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
DHT11_PIN = 16   # Grove D16 コネクタ

# ── サンプリング間隔 ─────────────────────────────────────────────────
# DHT11 は「1秒に1回まで」。それより速く読むと値が壊れるので 2秒あける
INTERVAL_SEC = 2

# ── 初期化 ───────────────────────────────────────────────────────────
sensor = dht.DHT11(Pin(DHT11_PIN))

print("DHT11 温湿度センサー 連続読み取り 開始")
print(f"{INTERVAL_SEC}秒ごとに読み取ります")
print("手で包む・息を吹きかけると湿度が上がる（反応は数秒〜十数秒かかる）")
print("-" * 40)

# ── メインループ ─────────────────────────────────────────────────────
while True:
    sensor.measure()
    print(f"温度: {sensor.temperature()} ℃  湿度: {sensor.humidity()} %")
    time.sleep(INTERVAL_SEC)
