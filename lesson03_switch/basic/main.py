from machine import Pin
import time

# ピン番号の定義
LED_PIN = 16     # D16コネクタ（GP16）
SWITCH_PIN = 18  # D18コネクタ（GP18）

# 待機時間の定義
SLEEP_TIME = 0.01  # 10ms

# スイッチ状態の定義（プルアップ接続）
SWITCH_PRESSED = 0   # スイッチが押されている状態
SWITCH_RELEASED = 1  # スイッチが離されている状態

# LED状態の定義
LED_ON = 1   # LED点灯
LED_OFF = 0  # LED消灯

# ピン設定
led = Pin(LED_PIN, Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

print("スイッチ入力プログラム開始")

# メインループ
while True:
    # スイッチの状態を読み取る
    switch_state = switch.value()
    
    if switch_state == SWITCH_PRESSED:
        led.value(LED_ON)
    else:
        led.value(LED_OFF)
    
    time.sleep(SLEEP_TIME)