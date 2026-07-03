# Raspberry Pi Pico 2W IoT電子工作講座

YouTube動画シリーズとブログ記事の連携教材リポジトリ。全12回構成のIoT入門コース。

## リポジトリ構造

```
lessonXX_name/   ← 各レッスンのコード（lesson02_, lesson03_...）
requirements.txt ← Python依存関係
```

## コーディング規約（MicroPython / Pico 2W）

- import文は冒頭にまとめる
- Wi-Fi接続は `wlan.isconnected()` でリトライ処理を必ず入れる
- センサー読み取り失敗時のフォールバック処理を含める
- Ambient送信は `try/except` で囲む
- コメントは日本語で記載（初心者が読むことを前提）
- Wi-FiパスワードやAPIキーはハードコードしない（定数・設定ファイルで分離）
- インデントはスペース4つ統一

## YouTube・ブログ連携ルール

- コードはブログ記事（thunderblog.org）と整合性を保つ
- レッスン番号・変数名・関数名はシリーズ全体で統一する
- 動画で説明する範囲を超えた複雑な実装は避ける（初心者が追えるレベルに保つ）
- 新しいlessonを追加する場合: `lessonXX_内容名/main.py` の形式で作成

## 対象読者

- IoT・電子工作の完全初心者
- PythonはなんとなくわかるがHWは初めての人
- MicroPython・Grove・Ambient・MQTTを使用
