from machine import ADC
import time
 
# ── 設定 ──────────────────────────────────────────────
LIGHT_PIN  = 26     # Grove A0 = GPIO26（ADC0）。※他ポートに挿す場合は 27/28 へ
ADC_MAX    = 65535  # read_u16() の最大値（16bit）
VREF       = 3.3    # Pico のADC基準電圧[V]
INTERVAL_S = 0.5    # 表示間隔[秒]
 
# ── 初期化 ────────────────────────────────────────────
light = ADC(LIGHT_PIN)
 
# 値域確認用（実行中の最小・最大を追従）
value_min = ADC_MAX
value_max = 0
 
print("=== Grove 光センサー 動作確認 ===")
print(f"ピン: GPIO{LIGHT_PIN} (A0/ADC0)")
print("センサーを覆う/明るくして値の変化を見てください（停止: Ctrl+C）\n")
 
# ── メインループ ──────────────────────────────────────
try:
    while True:
        try:
            value = light.read_u16()          # 0〜65535
        except Exception as e:                # 読み取り失敗時のフォールバック
            print(f"[WARN] 読み取り失敗: {e}")
            time.sleep(INTERVAL_S)
            continue
 
        voltage = VREF * value / ADC_MAX       # 電圧換算[V]
        percent = value / ADC_MAX * 100        # 明るさ[%]
        value_min = min(value_min, value)
        value_max = max(value_max, value)
 
        # 簡易バー（明るさを視覚化）
        bar = "#" * int(percent / 5)           # 0〜20文字
 
        print(
            f"raw={value:5d}  {voltage:4.2f}V  {percent:5.1f}%  "
            f"min={value_min:5d} max={value_max:5d}  |{bar:<20}|"
        )
        time.sleep(INTERVAL_S)

except KeyboardInterrupt:
    print("\n=== 終了 ===")
    print(f"観測した値域: min={value_min}  max={value_max}  "
          f"（幅={value_max - value_min}）")
    print("→ この min/max を lesson04 のしきい値設計に使ってください。")