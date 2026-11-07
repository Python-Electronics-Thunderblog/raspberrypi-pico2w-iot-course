# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Python Electronics Thunderblog
"""Grove 16x2 LCD（JHD1802・I2C 0x3E）用の最小ドライバ。

Raspberry Pi Pico 2W 講座 第6回のために自作したもので、
Seeed Studio 公式のライブラリではありません。
"""

import time

__all__ = ["GroveLCD"]


class GroveLCD:
    """Grove 16x2 LCD を I2C で動かすクラス。

    次の3種類に使えます（中身はほぼ同じ）。
        - Grove - 16 x 2 LCD (Black on Yellow)
        - Grove - 16 x 2 LCD (Black on Red)
        - Grove - 16 x 2 LCD (White on Blue)

    Args:
        i2c (machine.I2C): LCD をつないだ I2C バス。
        addr (int): LCD の I2C アドレス。初期値は 0x3E。
        cols (int): 1行の文字数。初期値は 16。
    """

    _CMD = 0x80   # 次のバイトはコマンド
    _DATA = 0x40  # 次のバイトは文字

    def __init__(self, i2c, addr=0x3E, cols=16):
        self._i2c = i2c
        self._addr = addr
        self._cols = cols
        time.sleep_ms(50)            # 電源が入ってから待つ
        for _ in range(3):
            self._command(0x28)      # 2行表示
            time.sleep_ms(5)
        self._command(0x0C)          # 表示ON・カーソルなし
        self.clear()
        self._command(0x06)          # 書くたびに右へ進む

    def _command(self, value):
        """LCD へコマンドを1つ送る（クラスの中だけで使う）。

        Args:
            value (int): 送るコマンド（0x00〜0xFF）。
        """
        self._i2c.writeto(self._addr, bytes((self._CMD, value)))

    def clear(self):
        """画面を全部消して、カーソルを左上へ戻す。"""
        self._command(0x01)
        time.sleep_ms(2)             # 消去は時間がかかる

    def move_to(self, col, row):
        """次に書く位置を決める。

        Args:
            col (int): 列（左から 0〜15）。
            row (int): 行（上が 0、下が 1）。
        """
        self._command(0x80 | (col + (0x40 if row else 0x00)))

    def write(self, text):
        """今のカーソル位置から文字を書く。

        Args:
            text (str): 表示する文字列（英数字と記号）。
        """
        for b in text.encode():
            self._i2c.writeto(self._addr, bytes((self._DATA, b)))

    def write_line(self, row, text):
        """1行を16文字にそろえて上書きする。

        短い文字列は空白で埋め、長い文字列は16文字で切るので、
        前に書いた文字が残りません。

        Args:
            row (int): 行（上が 0、下が 1）。
            text (str): 表示する文字列。
        """
        self.move_to(0, row)
        self.write(f"{text:<{self._cols}}"[: self._cols])
