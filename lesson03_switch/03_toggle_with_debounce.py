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
DEBOUNCE_TIME = 0.02  # 20ms 待機する

# ── ピン設定 ──────────────────────────────────────────────────
led    = Pin(LED_PIN,    Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN)

# ── 状態変数 ──────────────────────────────────────────────────
led_state             = LED_OFF          # LED の現在の状態
previous_switch_state = SWITCH_RELEASED  # 前回のスイッチ状態

led.value(led_state)
print("応用プログラム2 開始")

# ── メインループ ───────────────────────────────────────────────
while True:
    current_switch_state = switch.value()

    # スイッチが「はなす → 押す」に変わった瞬間だけ処理する
    if previous_switch_state == SWITCH_RELEASED and \
       current_switch_state  == SWITCH_PRESSED:

        # LED の状態を切り替える（ON ↔ OFF）
        if led_state == LED_OFF:
            led_state = LED_ON
        else:
            led_state = LED_OFF
        led.value(led_state)

        # チャタリング除去：20ms 待ってから次のループへ
        time.sleep(DEBOUNCE_TIME)

    # 前回の状態を更新してから次のループへ
    previous_switch_state = current_switch_state
