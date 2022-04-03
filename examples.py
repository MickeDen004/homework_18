# from dataclasses import dataclass
# from random import shuffle
#
# @dataclass
# class Card_deck:
#     deck = []
#     broadway = ['J', 'Q', 'K', 'A']
#     suit = ['h', 'd', 'c', 's']
#     def create_deck(self):
#         for suit in self.suit:
#             for i in range(2, 11):
#                 self.deck.append(str(i)+suit)
#             for i in self.broadway:
#                 self.deck.append(i+suit)
#
#     def shuffle(self):
#         shuffle(self.deck)
#
#     def hand_out(self, player):
#         for i in range(player):
