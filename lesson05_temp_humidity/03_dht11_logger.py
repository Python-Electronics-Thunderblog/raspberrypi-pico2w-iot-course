from machine import Pin
import dht
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
DHT11_PIN = 16   # Grove D16 コネクタ

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 2   # DHT11 は「1秒に1回まで」

# ── チェックサム失敗のメッセージ ─────────────────────────────────────
# MicroPython の dht ドライバは、チェックサムが合わないと
# OSError ではなく Exception("checksum error") を投げる
CHECKSUM_ERROR_MSG = "checksum error"

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
        # センサーから返事が来なかった（タイムアウト）
        #   ・ケーブルが抜けている / 接触不良
        print("センサーから応答がありません:", e)
    except Exception as e:
        # 40ビットの最後のチェックサムが合わなかった
        # Exception はほとんどすべてのエラーの親。そのまま受け止めると
        # 打ち間違いのような本当のバグまで飲み込んでしまうので、
        # checksum error 以外は raise でそのまま止める
        if str(e) != CHECKSUM_ERROR_MSG:
            raise
        print("データが正しく届きませんでした:", e)

    time.sleep(INTERVAL_SEC)
