# Raspberry Pi Pico 2W で始めるIoT電子工作入門

このリポジトリは、Raspberry Pi Pico 2Wを使ったIoT電子工作入門講座のサンプルコードと学習資料を提供します。MicroPythonを使用して、基礎から実践的なIoTプロジェクトまでを段階的に学習できるように構成されています。

## 目次

- [講座の概要](#-講座の概要)
- [特徴](#-特徴)
- [対象者](#-対象者)
- [必要なもの](#-必要なもの)
- [環境構築](#-環境構築)
- [レッスン一覧](#-レッスン一覧)
- [ディレクトリ構造](#-ディレクトリ構造)
- [使い方](#-使い方)
- [トラブルシューティング](#-トラブルシューティング)
- [リソース](#-リソース)
- [ライセンス](#-ライセンス)
- [コントリビューション](#-コントリビューション)

## 📚 講座の概要

Raspberry Pi Pico 2Wは、Raspberry Pi財団が提供する低価格で高性能なマイコンボードです。本講座では、MicroPythonを使用して、電子工作の基礎からIoTデバイスの開発まで、実践的なプロジェクトを通じて学習します。

**Raspberry Pi Pico 2Wの主な特徴:**
- RP2350マイコン搭載（デュアルコアArm Cortex-M33 @ 150MHz）
- 520KB SRAM、4MB フラッシュメモリ
- Wi-Fi（2.4GHz 802.11n）およびBluetooth 5.2対応
- 26本のGPIOピン（うち3本はADC対応）
- PWM、I2C、SPI、UART対応
- 低消費電力設計

## ✨ 特徴

- **初心者向け**: プログラミングや電子工作の経験がなくても学習できる段階的な構成
- **実践的**: 実際に動作するプロジェクトを通じて学習
- **MicroPython使用**: わかりやすく学びやすいプログラミング言語
- **IoT対応**: Wi-Fi機能を活用したIoTデバイスの開発
- **豊富なサンプルコード**: すぐに試せるコード例を多数収録
- **日本語ドキュメント**: すべての資料が日本語で提供

## 🎯 対象者

- 電子工作やプログラミングに興味がある初心者
- IoTデバイスの開発を始めたい方
- MicroPythonを学びたい方
- Raspberry Pi Pico 2Wの使い方を知りたい方
- ものづくりやプロトタイピングに興味がある方
- STEM教育に携わる教育者の方

## 📋 必要なもの

### ハードウェア

#### 基本セット
- **Raspberry Pi Pico 2W** × 1
- **USB Type-Cケーブル** × 1（データ転送対応）
- **ブレッドボード** × 1（400穴または830穴）
- **ジャンパーワイヤー** × 適量（オス-オス、オス-メス）

#### レッスンごとに必要な電子部品
各レッスンのREADME.mdに詳細な部品リストを記載しています。

**よく使用する部品:**
- LED（赤、緑、青など）
- 抵抗（220Ω、1kΩ、10kΩなど）
- タクトスイッチ
- センサー類（温湿度センサー、距離センサーなど）
- サーボモーター
- その他（レッスンごとに指定）

### ソフトウェア

#### PC側の環境
- **Python 3.7以上**: スクリプトやツールの実行に必要
- **Thonny IDE**（推奨）: 初心者に優しいMicroPython開発環境
  - ダウンロード: https://thonny.org/
- **その他のツール**: requirements.txtに記載

#### Pico 2W側
- **MicroPythonファームウェア**: Pico 2Wで実行

## 🚀 環境構築

### 1. Pythonツールのインストール

リポジトリをクローンして、必要なツールをインストールします。

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/raspberrypi-pico2w-iot-course.git
cd raspberrypi-pico2w-iot-course

# 必要なツールをインストール
pip install -r requirements.txt
```

### 2. Thonny IDEのインストール

Thonnyは初心者に優しいPython IDEで、MicroPythonの開発に最適です。

1. [Thonny公式サイト](https://thonny.org/)から、お使いのOSに対応したバージョンをダウンロード
2. ダウンロードしたインストーラーを実行してインストール
3. インストール完了後、Thonnyを起動

### 3. MicroPythonファームウェアのインストール

Raspberry Pi Pico 2WにMicroPythonファームウェアをインストールします。

#### 手順:

1. **BOOTSELモードで接続**
   - Raspberry Pi Pico 2WのBOOTSELボタンを押しながらUSBケーブルでPCに接続
   - ドライブとして「RPI-RP2」がマウントされる

2. **ファームウェアのダウンロード**
   - [MicroPython公式ダウンロードページ](https://micropython.org/download/RPI_PICO2/)にアクセス
   - Raspberry Pi Pico 2W用の最新ファームウェア（.uf2ファイル）をダウンロード
   - ファイル名例: `RPI_PICO2W-YYYYMMDD-vX.XX.X.uf2`

3. **ファームウェアの書き込み**
   - ダウンロードした.uf2ファイルを、マウントされた「RPI-RP2」ドライブにドラッグ&ドロップ
   - 自動的に再起動し、MicroPythonが起動

4. **確認**
   - Pico 2WのLEDが点滅したら成功

### 4. Thonnyの設定

Thonnyを使用してPico 2Wと通信できるように設定します。

1. Thonnyを起動
2. メニューから「ツール」→「オプション」を選択（Macの場合は「Thonny」→「設定」）
3. 「インタープリタ」タブを選択
4. インタープリタのドロップダウンから**「MicroPython (Raspberry Pi Pico)」**を選択
5. ポートを選択（通常は自動検出されます）
   - Windows: `COMx`
   - macOS: `/dev/cu.usbmodem...`
   - Linux: `/dev/ttyACM0`
6. 「OK」をクリックして設定を保存

### 5. 動作確認

ThonnyのREPLシェル（下部のウィンドウ）に以下のように表示されれば成功です:

```
MicroPython v1.xx.x on YYYY-MM-DD; Raspberry Pi Pico 2W with RP2350
Type "help()" for more information.
>>>
```

簡単なテストコードを実行してみましょう:

```python
>>> print("Hello, Pico 2W!")
Hello, Pico 2W!
```

## 📖 レッスン一覧

各レッスンは独立したディレクトリに分かれており、サンプルコードとREADME.mdが含まれています。

### Lesson 01: はじめに（環境構築）
- Raspberry Pi Pico 2Wの概要
- 開発環境のセットアップ
- MicroPythonファームウェアのインストール
- Hello World（LED点灯）

**学習内容:**
- Pico 2Wの基本構造
- MicroPythonの基礎
- 最初のプログラム

### Lesson 02: セットアップと基本操作
- MicroPythonの基礎文法
- REPL（対話型シェル）の使い方
- ファイルの転送方法
- GPIOピンの基本操作

**学習内容:**
- 変数とデータ型
- 条件分岐とループ
- 関数の定義
- ファイル操作

### Lesson 03以降（今後追加予定）

以下のレッスンを順次追加予定です:

- **Lesson 03**: デジタル入出力（ボタンとLED）
- **Lesson 04**: PWM制御（LEDの明るさ調整）
- **Lesson 05**: アナログ入力（センサーの読み取り）
- **Lesson 06**: Wi-Fi接続
- **Lesson 07**: Webサーバーの構築
- **Lesson 08**: センサーデータの収集と送信
- **Lesson 09**: MQTTプロトコル
- **Lesson 10**: 実践プロジェクト

## 📁 ディレクトリ構造

```
raspberrypi-pico2w-iot-course/
├── README.md                 # 本ファイル（プロジェクトの全体説明）
├── .gitignore               # Git無視ファイル設定
├── requirements.txt         # PC側で必要なPythonツール
├── LICENSE                  # ライセンス情報（MIT）
├── lesson02_set_up/        # レッスン02のコードと資料
│   ├── README.md           # レッスン02の説明
│   ├── examples/           # サンプルコード
│   └── exercises/          # 演習問題
└── (今後のレッスンフォルダ)
```

## 💡 使い方

### 1. サンプルコードの実行

1. Thonnyで学びたいレッスンのディレクトリを開く
2. サンプルコードファイル（.py）を開く
3. 「実行」ボタン（緑の再生ボタン）をクリック

### 2. コードをPico 2Wに保存

プログラムをPico 2Wに保存すると、電源を入れるたびに自動実行されます。

1. Thonnyでコードを開く
2. 「ファイル」→「名前を付けて保存」を選択
3. 保存先で**「Raspberry Pi Pico」**を選択
4. ファイル名を`main.py`として保存

### 3. ファイル転送ツールの使用

Thonny以外のツールでファイル転送する場合:

```bash
# rshellを使用
rshell
> cp local_file.py /pyboard/

# ampyを使用
ampy --port /dev/ttyACM0 put local_file.py
```

## 🔧 トラブルシューティング

### Raspberry Pi Pico 2Wが認識されない

**原因と対処法:**
- USBケーブルがデータ転送対応か確認（充電専用ケーブルでは認識されません）
- 別のUSBポートで試す
- デバイスドライバが正しくインストールされているか確認
- BOOTSELボタンを押しながら接続し、ファームウェアを再インストール

### Thonnyで接続できない

**原因と対処法:**
- 正しいインタープリタとポートが選択されているか確認
- 他のアプリケーション（Arduinoシリアルモニタなど）がポートを使用していないか確認
- Raspberry Pi Pico 2Wを一度抜いて再接続
- Thonnyを再起動
- ファームウェアを再インストール

### プログラムが動作しない

**原因と対処法:**
- エラーメッセージを確認（REPLシェルに表示されます）
- インデント（字下げ）が正しいか確認（Pythonではインデントが重要）
- ピン番号が正しいか確認
- 配線が正しいか確認（ブレッドボードの接続）
- 部品の極性が正しいか確認（LEDなど）

### Wi-Fiに接続できない

**原因と対処法:**
- SSID（ネットワーク名）とパスワードが正しいか確認
- 2.4GHz帯のWi-Fiを使用しているか確認（5GHz帯は非対応）
- ルーターの設定でMACアドレスフィルタリングが有効になっていないか確認
- セキュリティ設定がWPA2/WPA3であることを確認

### メモリエラーが発生する

**原因と対処法:**
- 大きなライブラリやデータを扱っている場合、メモリ不足の可能性
- 不要な変数やオブジェクトを削除
- ガベージコレクションを明示的に実行: `import gc; gc.collect()`
- プログラムを分割して実行

## 📚 リソース

### 公式ドキュメント
- [Raspberry Pi Pico 2W公式ページ](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
- [MicroPython公式ドキュメント](https://docs.micropython.org/)
- [MicroPython RP2ドキュメント](https://docs.micropython.org/en/latest/rp2/quickref.html)

### 学習リソース
- [Thonny公式サイト](https://thonny.org/)
- [Python公式チュートリアル（日本語）](https://docs.python.org/ja/3/tutorial/)
- [MicroPython入門](https://micropython-docs-ja.readthedocs.io/)

### コミュニティ
- [Raspberry Pi Forums](https://forums.raspberrypi.com/)
- [MicroPython Forum](https://forum.micropython.org/)

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

自由に学習、改変、配布していただけます。商用利用も可能です。

## 🤝 コントリビューション

プルリクエストや問題の報告を歓迎します。

### コントリビューション方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 改善提案

改善提案がある場合は、お気軽にIssueを開いてください。以下のような提案を歓迎します:

- 新しいレッスンのアイデア
- サンプルコードの改善
- ドキュメントの誤りや改善
- 新しいプロジェクトの提案

## 📞 お問い合わせ

質問や提案がある場合は、GitHubのIssueを通じてお問い合わせください。

---

**Happy Coding! 🚀**

Raspberry Pi Pico 2Wで楽しいIoT電子工作をお楽しみください！
