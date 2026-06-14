from machine import Pin
import time

# ── ピン番号の定義 ─────────────────────────────────────────────
LED_PIN    = 16   # LEDをつなぐピン（GP16）
SWITCH_PIN = 18   # スイッチをつなぐピン（GP18）

# ── 状態の定義（Grove Button はプルダウン接続） ────────────────
SWITCH_PRESSED  = 1  # 押している → 1
SWITCH_RELEASED = 0  # はなしている → 0
LED_ON  = 1
LED_OFF = 0

# ── チャタリング除去の待機時間 ─────────────────────────────────
DEBOUNCE_MS = 20  # 20ms 以内の再入力はチャタとして無視

# ── ピン設定 ──────────────────────────────────────────────────
led    = Pin(LED_PIN,    Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN)

# ── 状態変数 ──────────────────────────────────────────────────
led_state             = LED_OFF
previous_switch_state = SWITCH_RELEASED
last_press_time       = time.ticks_ms()  # 最後に押下を確定した時刻
count = 0                                 # 押された回数

led.value(led_state)
print("応用プログラム 開始")

# ── メインループ ───────────────────────────────────────────────
while True:
    current_switch_state = switch.value()

    # スイッチが「はなす → 押す」に変わった瞬間（立ち上がりエッジ）
    if previous_switch_state == SWITCH_RELEASED and \
       current_switch_state == SWITCH_PRESSED:

        now = time.ticks_ms()
        # 前回の確定から DEBOUNCE_MS 以上たっていれば本物の押下
        if time.ticks_diff(now, last_press_time) > DEBOUNCE_MS:
            count += 1

            # LED状態を切り替える（OFFならON、そうでなければOFF）
            if led_state == LED_OFF:
                led_state = LED_ON
            else:
                led_state = LED_OFF
            led.value(led_state)

            print("押された回数:", count)
            last_press_time = now

    # 前回の状態を更新してから次のループへ
    previous_switch_state = current_switch_state
