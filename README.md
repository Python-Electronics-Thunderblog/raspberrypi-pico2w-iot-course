# Raspberry Pi Pico 2W で始めるIoT電子工作入門

このリポジトリは、Raspberry Pi Pico 2Wを使ったIoT電子工作入門講座のサンプルコードと学習資料を提供します。

## 📚 講座の概要

Raspberry Pi Pico 2Wは、Raspberry Pi財団が提供する低価格で高性能なマイコンボードです。本講座では、MicroPythonを使用して、基礎から実践的なIoTプロジェクトまでを学習します。

## 🎯 対象者

- 電子工作やプログラミングに興味がある初心者
- IoTデバイスの開発を始めたい方
- MicroPythonを学びたい方
- Raspberry Pi Pico 2Wの使い方を知りたい方

## 📋 必要なもの

### ハードウェア
- Raspberry Pi Pico 2W
- USB Type-Cケーブル
- ブレッドボード
- ジャンパーワイヤー
- 各種電子部品（LED、抵抗、センサーなど - レッスンごとに記載）

### ソフトウェア
- Python 3.7以上
- Thonny IDE（推奨） - https://thonny.org/
- その他の必要なツール（requirements.txt参照）

## 🚀 環境構築

### 1. Pythonツールのインストール

```bash
pip install -r requirements.txt
```

### 2. Thonny IDEのインストール

Thonnyは初心者に優しいPython IDEで、MicroPythonの開発に最適です。

- [Thonny公式サイト](https://thonny.org/)からダウンロードしてインストール

### 3. MicroPythonファームウェアのインストール

1. Raspberry Pi Pico 2WのBOOTSELボタンを押しながらUSBケーブルでPCに接続
2. ドライブとしてマウントされる
3. [MicroPython公式サイト](https://micropython.org/download/)から最新のファームウェア(.uf2ファイル)をダウンロード
4. ダウンロードしたファイルをマウントされたドライブにコピー
5. 自動的に再起動し、MicroPythonが起動

### 4. Thonnyの設定

1. Thonnyを起動
2. メニューから「ツール」→「オプション」を選択
3. 「インタープリタ」タブで「MicroPython (Raspberry Pi Pico)」を選択
4. ポートを選択（通常は自動検出）

## 📖 レッスン一覧

### Lesson 01: はじめに（環境構築）
- Raspberry Pi Pico 2Wの概要
- 開発環境のセットアップ
- Hello World（LED点灯）

### Lesson 02: セットアップと基本操作
- MicroPythonの基礎
- REPL（対話型シェル）の使い方
- ファイルの転送方法

### Lesson 03以降
（今後追加予定）

## 📁 ディレクトリ構造

```
raspberrypi-pico2w-iot-course/
├── README.md                 # 本ファイル
├── .gitignore               # Git無視ファイル設定
├── requirements.txt         # 必要なPCツール
├── LICENSE                  # ライセンス情報
├── lesson02_set_up/        # レッスン02のコードと資料
└── (今後のレッスンフォルダ)
```

## 🔧 トラブルシューティング

### Raspberry Pi Pico 2Wが認識されない
- USBケーブルがデータ転送対応か確認
- 別のUSBポートで試す
- デバイスドライバが正しくインストールされているか確認

### Thonnyで接続できない
- 正しいインタープリタとポートが選択されているか確認
- 他のアプリケーションがポートを使用していないか確認
- Raspberry Pi Pico 2Wを再接続

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🤝 コントリビューション

プルリクエストや問題の報告を歓迎します。改善提案がある場合は、お気軽にIssueを開いてください。

## 📞 お問い合わせ

質問や提案がある場合は、GitHubのIssueを通じてお問い合わせください。

---

Happy Coding! 🎉
