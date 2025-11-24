from machine import Pin
import time

# LEDピンの設定
LED_PIN = 16
# 点滅間隔（秒）
INTERVAL = 0.1  

# LEDの準備
led = Pin(LED_PIN, Pin.OUT)

# 点滅を繰り返す
while True:
    led.on()
    time.sleep(INTERVAL)
    led.off()
    time.sleep(INTERVAL)
