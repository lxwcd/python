# -*- coding: utf-8 -*-
#
# Time: 2024-01-11
# File: blackjack.py
# URL:
#   代码参考：https://www.askpython.com/python/examples/blackjack-game-using-python
#   代码参考：https://www.youtube.com/watch?v=aryte85bt_M&ab_channel=Beau
#   牌显示代码：https://copyprogramming.com/howto/ascii-fication-of-playing-cards
#   绘制牌边框unicode码：https://unicode.org/charts/nameslist/n_2500.html
# Description: 21 点扑克牌游戏，学习使用

import random
import os
import textwrap


# clear the terminal
def clear():
    clear_command = "cls" if os.name == "nt" else "clear" if os.name == "posix" else ""
    os.system(clear_command)


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

    def __init__(self, suit: str, rank: str):
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

    # def show(self):
    #     lines = []
    #     space = '' if self.rank == '10' else ' '
    #     lines.append('┌───────┐')
    #     lines.append('|{}{}     |'.format(self.rank, space))
    #     lines.append('|       |')
    #     lines.append('|   {}   |'.format(self.suit_value))
    #     lines.append('|       |')
    #     lines.append('|     {}{}|'.format(space, self.rank))
    #     lines.append('└───────┘')
    #
    #     return '\n'.join(lines)

    def list_of_card(self):
        return self.__str__().splitlines()

    @staticmethod
    def ascii_of_hidden_card():
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

    @staticmethod
    def list_of_hidden_card():
        return Card.ascii_of_hidden_card().splitlines()

    def text_of_card(self):
        return f'{self.suits_values[self.suit]}{self.rank}: {self.card_value}'


# card1 = Card('Spades', 'K')
# card2 = Card('Spades', 'J')
# card3 = Card('Hearts', '10')
# print(card1.show())
# print(card2.list_of_card())
# print(card3.ascii_of_hidden_card())
# print(card1.text_of_card())

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits_values.keys()
                      for rank in Card.cards_values.keys()]

    # 洗牌
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # 发牌
    def deal(self):
        if self.cards:
            return self.cards.pop()


# 玩家或庄家手中的牌
class Hand:
    def __init__(self, is_dealer=False):
        self.cards = []
        self.list_cards = []  # 每个元素 card 为 list，方便后面绘制牌
        self.score = 0
        self.is_dealer = is_dealer

    # 添加牌
    def add_card(self, card: Card):
        self.cards.append(card)
        self.list_cards.append(card.list_of_card())

    # 计算牌的大小
    def cal_score(self):
        self.score = 0
        num_aces = 0
        for card in self.cards:
            num_aces += 1 if card.rank == 'A' else 0
            self.score += int(card.card_value)

        # 根据牌的大小设置 A 的值，超过 21 则做 1 计算
        while self.score > 21 and num_aces > 0:
            self.score -= 10
            num_aces -= 1

        return self.score

    def is_blackjack(self):
        return self.cal_score() == 21

    # 横向展示多张牌
    def display_cards(self, game_over=False):
        role = 'DEALER' if self.is_dealer else 'PLAYER'
        hide_card = not game_over and self.is_dealer
        list_cards = []

        # 庄家隐藏第一张牌
        if self.cards:
            list_cards = self.cards[0].list_of_hidden_card() if hide_card else self.list_cards[0]

        num_card = len(self.list_cards)
        # 每个列表（一张牌）的像同行组合为一个新列表的一行，多张牌横向展示
        if num_card > 1:
            list_cards = zip(list_cards, *self.list_cards[1:])

        # print cards horizontally, use two tabs as delimiter
        # items is tuple
        # str(item) for item in items 为生成器表达式
        deli_card = '\t' if num_card > 1 else ''
        result_list = [deli_card.join(str(item) for item in items) for items in list_cards]

        print(f'{role} CARDS: ')
        print('\n'.join(result_list))

        if not hide_card:
            print(f'{role} SCORE = ', self.cal_score())

        print("=" * 80, "\n") if self.is_dealer else None


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(is_dealer=True)

    def play(self):
        clear()
        # 初始玩家和庄家各发两张牌
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.player_hand.display_cards()

            input()

            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.display_cards()

            input()

        # 结束游戏
        if self.check_winner():
            return

        # 继续游戏，玩家选择是否要牌
        choice = ""
        while self.player_hand.cal_score() < 21 and choice not in ["s", "stand"]:
            choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
            while choice not in ["h", "s", "hit", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
                print()

            if choice in ["hit", "h"]:
                self.add_and_show_card(self.player_hand)

        if self.check_winner():
            return

        # 玩家停牌
        while self.dealer_hand.cal_score() < 17:
            self.add_and_show_card(self.dealer_hand, True)

        self.check_winner(True)

    def add_and_show_card(self, hand: Hand, game_over: bool = False):
        clear()
        hand.add_card(self.deck.deal())
        self.player_hand.display_cards()
        print("\n")
        self.dealer_hand.display_cards(game_over)

    def check_winner(self, game_over: bool = False):
        self.player_hand.cal_score()
        self.dealer_hand.cal_score()

        is_over = True
        result = ""

        if not game_over:
            if self.player_hand.score > 21:
                result = "You busted. Dealer wins! 😭"
            elif self.dealer_hand.score > 21:
                result = "Dealer busted. You win! 😄"
            elif self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
                result = "Both players have blackjack! Tie! 😑"
            elif self.player_hand.is_blackjack():
                result = "You have blackjack. You win! 😄"
            elif self.dealer_hand.is_blackjack():
                result = "Dealer has blackjack. Dealer wins! 😭"
            else:
                is_over = False
        else:
            if self.player_hand.score > self.dealer_hand.score:
                result = "You win! 😄"
            elif self.player_hand.score == self.dealer_hand.score:
                result = "Tie! 😑"
            else:
                result = "Dealer wins. 😭"

        if is_over:
            clear()
            self.player_hand.display_cards()
            print("\n")
            self.dealer_hand.display_cards(game_over=True)
            print(f"\n{result}")

        return is_over


def main():
    game = BlackJack()
    game.play()

if __name__ == '__main__':
    main()
