from machine import Pin
import dht
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
DHT11_PIN = 16   # Grove D16 コネクタ

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 2   # DHT11 は「1秒に1回まで」

# ── 初期化 ───────────────────────────────────────────────────────────
sensor = dht.DHT11(Pin(DHT11_PIN))

print("DHT11 温湿度センサー 連続読み取り（エラー対策あり）開始")
print("ケーブルを抜いてもプログラムは止まりません")
print("-" * 40)

# ── メインループ ─────────────────────────────────────────────────────
while True:
    # try/except は「エラーを隠す道具」ではなく
    # 「止まってほしくない場所を守る道具」
    try:
        sensor.measure()
        print(f"温度: {sensor.temperature()} ℃  湿度: {sensor.humidity()} %")
    except OSError as e:
        # 読み取り失敗の主な原因
        #   ・ケーブルが抜けている / 接触不良 → タイムアウト
        #   ・40ビットの最後のチェックサムが合わない
        # except の後ろに OSError と型を書くのが大事。
        # 何でも受け止める except: は、本当のバグまで飲み込んでしまう
        print("センサーの読み取りに失敗しました:", e)

    time.sleep(INTERVAL_SEC)
