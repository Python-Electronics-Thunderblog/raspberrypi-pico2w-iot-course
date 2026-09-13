from machine import Pin
import dht
import time

# ── ピン設定 ─────────────────────────────────────────────────────────
DHT11_PIN = 16   # Grove D16 コネクタ

# ── サンプリング間隔 ─────────────────────────────────────────────────
INTERVAL_SEC = 2   # DHT11 は「1秒に1回まで」

# ── 保存先ファイル ───────────────────────────────────────────────────
# Pico 本体のフラッシュに保存する。Thonny の「ファイル」欄から PC へダウンロードできる
LOG_FILE = "dht11_log.csv"
# 見出しは英語にする。日本語で書くと、Excel で開いたときに文字化けする
CSV_HEADER = "sec,temp,humidity\n"
MS_PER_SEC = 1000

# ── 初期化 ───────────────────────────────────────────────────────────
sensor = dht.DHT11(Pin(DHT11_PIN))

# 実行するたびにファイルを作り直し、1行目に見出しを書く
# （"w" は上書き。前回の記録を残したいときは、先に PC へダウンロードしておく）
try:
    with open(LOG_FILE, "w") as f:
        f.write(CSV_HEADER)
except OSError as e:
    print("ファイルを作れませんでした:", e)

# 時刻は「経過秒」にする。PC につながずに動かすと Pico の時計は正しい日時にならないため
start_ms = time.ticks_ms()

print("DHT11 温湿度センサー CSV 保存 開始")
print(f"{INTERVAL_SEC}秒ごとに {LOG_FILE} へ1行ずつ追記します")
print("止めるときは Thonny の停止ボタン。止めてからファイルをダウンロードします")
print("-" * 40)

# ── メインループ ─────────────────────────────────────────────────────
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humi = sensor.humidity()
        elapsed_sec = time.ticks_diff(time.ticks_ms(), start_ms) // MS_PER_SEC

        # "a" は追記。1行書くたびに閉じるので、途中で止めても書いた行は残る
        with open(LOG_FILE, "a") as f:
            f.write(f"{elapsed_sec},{temp},{humi}\n")

        print(f"{elapsed_sec}秒  温度: {temp} ℃  湿度: {humi} %")
    except OSError as e:
        # センサーの読み取り失敗も、ファイルの書き込み失敗も OSError で届く
        # 失敗した回は行を書かずに飛ばし、次の読み取りへ進む
        print("読み取りか保存に失敗しました:", e)

    time.sleep(INTERVAL_SEC)
