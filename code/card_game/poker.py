# -*- coding: utf-8 -*-
#
# Time: 2024-01-11
# File: poker.py
# URL: https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第19课：面向对象编程应用.md#案例1扑克游戏
# Description: 扑克牌游戏 github 代码示例，学习用


from enum import Enum
import random


# 牌的花色
class Suit(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)


# for suit in Suit:
#     print(f'{suit}:{suit.value}')


# 纸牌
class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def __repr__(self):
        suits = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suits[self.suit.value]}{faces[self.face]}'

    def __lt__(self, other):
        """重载运算符 < """
        if self.suit == other.suit:
            return self.face < other.face

        return self.suit.value < other.suit.value


"""
card1 = Card(Suit.SPADE, 5)
card2 = Card(Suit.HEART, 11)
print(card1, card2)
"""


# 扑克
class Poker:
    def __init__(self):
        # 列表生成式，双重 for 循环，生成 52 张牌
        self.cards = [Card(suit, face) for suit in Suit
                      for face in range(1, 14)]
        # 发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """是否还有牌"""
        return self.current < len(self.cards)


"""
poker = Poker()
poker.shuffle()
print(poker.cards)
"""


# 玩家
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('小赵'), Player('小钱'), Player('小孙'), Player('小李')]

    for _ in range(13):
        for player in players:
            player.get_one(poker.deal())

    for player in players:
        player.arrange()
        print(f'{player.name}: ', end='')
        print(player.cards)


if __name__ == '__main__':
    main()
