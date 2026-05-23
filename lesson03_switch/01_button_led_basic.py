from machine import Pin
import time

# ピン番号の定義
LED_PIN    = 16    # LEDをつなぐピン（GP16 = D16コネクタ）
SWITCH_PIN = 18    # スイッチをつなぐピン（GP18 = D18コネクタ）

# 待機時間の定義
SLEEP_TIME = 0.01  # 10ms ごとにスイッチを確認する

# スイッチ状態の定義
SWITCH_PRESSED  = 1  # スイッチが押されている状態
SWITCH_RELEASED = 0  # スイッチが離されている状態

#LED状態の定義
LED_ON  = 1  # LED点灯
LED_OFF = 0  # LED消灯

# ピン設定
led    = Pin(LED_PIN,    Pin.OUT)              # LED：出力として設定
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_DOWN) # スイッチ：入力（プルアップ）として設定

print("スイッチ入力プログラム開始")

# メインループ
while True:
    # スイッチの現在の状態を読み取る（0 または 1 が返る）
    switch_state = switch.value()

    if switch_state == SWITCH_PRESSED:   # スイッチを押しているとき
        led.value(LED_ON)                # → LED を点灯
    else:                                # スイッチをはなしているとき
        led.value(LED_OFF)               # → LED を消灯

    time.sleep(SLEEP_TIME)  # 少し待ってから次のループへ