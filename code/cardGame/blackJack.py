# -*- coding: utf-8 -*-
#
# Time: 2024-01-11
# File: blackJack.py
# URL:
#   主要程序代码：https://www.askpython.com/python/examples/blackjack-game-using-python
#   牌显示代码：https://copyprogramming.com/howto/ascii-fication-of-playing-cards
#   绘制牌边框unicode码：https://unicode.org/charts/nameslist/n_2500.html
# Description: 21 点扑克牌游戏，学习使用

import random
import os
import time
import textwrap


class Card:
    suits_values = {
        'Spades': "\u2660",
        'Hearts': "\u2665",
        'Clubs': "\u2663",
        'Diamonds': "\u2666"
    }
    cards_values = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spades
        :param rank: The value of the card, e.g. A
        """
        self.suit = suit
        self.rank = rank
        self.suit_value = self.suits_values[self.suit]
        self.card_value = self.cards_values[rank]

    # ascii version of card
    def __str__(self):
        """
        :lines: 第一个参数为数字，占两位，左对齐，除了 10 其他只占用一个字符宽度
        :lines: 第二个参数为数字，占一位，花色图案
        :lines: 第三个参数为数字，占两位，右对齐，除了 10 其他只占用一个字符宽度
        """
        lines = """\
        ┌───────┐
        |{}     |
        |       |
        |   {}  |
        |       |
        |     {}|
        └───────┘
        """.format('{rank: <2}', '{suit_value: <2}', '{rank: >2}')

        # 另一种方式，书写不美观，且麻烦
        # lines = [[] for i in range(7)]
        # space = '' if self.rank == '10' else ' '
        # lines[0].append('┌───────┐')
        # lines[1].append('|{}{}     |'.format(self.rank, space))
        # lines[2].append('|       |')
        # lines[3].append('|   {}   |'.format(self.suit_value))
        # lines[4].append('|       |')
        # lines[5].append('|     {}{}|'.format(space, self.rank))
        # lines[6].append('└───────┘')
        # result = [''.join(line) for line in lines]
        # return '\n'.join(result)

        return textwrap.dedent(lines.format(rank=self.rank, suit_value=self.suit_value))

    def ascii_of_hidden_card(self):
        lines = """\
        ┌───────┐
        |░░░░░░░|
        |░░░░░░░|
        |░░░░░░░|
        |░░░░░░░|
        |░░░░░░░|
        └───────┘
        """
        return textwrap.dedent(lines)

    def text_of_card(self):
        return f'{self.suits_values[self.suit]}{self.rank}: {self.card_value}'


card1 = Card('Spades', 'K')
card2 = Card('Spades', 'J')
card3 = Card('Hearts', '10')
print(card2)
print(card3.ascii_of_hidden_card())
print(card1.text_of_card())
