#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:
    High Card : Highest value card.
    One Pair : Two cards of the same value.
    Two Pairs : Two different pairs.
    Three of a Kind : Three cards of the same value.
    Straight : All cards are consecutive values.
    Flush : All cards of the same suit.
    Full House : Three of a kind and a pair.
    Four of a Kind : Four cards of the same value.
    Straight Flush : All cards are consecutive values of same suit.
    Royal Flush : Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same
ranked hands then the rank made up of the highest value wins; for
example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if
the highest cards tie then the next highest cards are compared, and so
on. Consider the following five hands dealt to two players: Hand
Player 1 Player 2 Winner 1 5H 5C 6S 7S KD Pair of Fives 2C 3S 8S 8D TD
Pair of Eights Player 2 2 5D 8C 9S JS AC Highest card Ace 2C 5C 7D 8S
QH Highest card Queen Player 1 3 2D 9C AS AH AC Three Aces 3D 6D 7D TD
QD Flush  with Diamonds Player 2 4 4D 6S 9H QH QC Pair of Queens
Highest card Nine 3D 6D 7H QD QS Pair of Queens Highest card Seven
Player 1 5 2H 2D 4C 4D 4S Full House With Three Fours 3C 3D 3S 9S 9D
Full House with Three Threes Player 1 The file, poker.txt , contains
one-thousand random hands dealt to two players. Each line of the file
contains ten cards (separated by a single space): the first five are
Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand
there is a clear winner. How many hands does Player 1 win?

Answer: 376
"""
from __future__ import print_function
from utils import timer
from collections import Counter

_MAP_VALUES = 'TJQKA'


def map_value(v):
    """
    Map Ten, Jack, Queen, King, Ace to increasing values
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
    """
    if v in _MAP_VALUES:
        return 10 + _MAP_VALUES.index(v)
    else:
        return int(v)


with open('./data/054_poker_hands.txt', 'r') as f:
    DATA = f.readlines()
    HANDS = []
    for x in DATA:
        hand_a = [(map_value(value), suit) for value, suit in x.split()[:5]]
        hand_b = [(map_value(value), suit) for value, suit in x.split()[5:]]
        HANDS.append((hand_a, hand_b))


def hand_value(hand):
    """
    Creates a tuple representng hand value.
    I.e

    High card   = (0, xx)
    1 pair      = (1, xx)
    2 pair      = (2, xx)
    3ook        = (3, xx)
    straight    = (4, xx)
    flush       = (5, xx)
    full house  = (6, xx)
    4ook        = (7, xx)
    str flush   = (8, xx)
    royal flush = (9, xx)
    """
    cards = Counter([c for c, s in hand])
    suits = Counter([s for c, s in hand])
    reverse_cards = sorted(cards.keys(), reverse=True)
    hc = reverse_cards[0]
    straight = is_straight(reverse_cards)

    if len(suits) == 1:
        # Flush, Straight Flush or Royal Flush
        if straight:
            if hc == 14:
                return (9, None)
            else:
                return (8, hc)
        else:
            return (5, None)

    if len(cards) == 2:
        # four of a kind  or  full house
        # Output the pairs is reverse sort order then the remainder of the
        # cards in reverese sort order
        val, amm = cards.most_common()[0]
        if amm == 4:
            x = set((val,)) ^ set(reverse_cards)
            return (7, [val] + sorted(x, reverse=True))
        else:
            val2, _ = cards.most_common()[1]
            return (6, [val, val2])

    if len(cards) == 3:
        # Three of a kind  or  Two pair
        val, amm = cards.most_common()[0]
        val2, _ = cards.most_common()[1]
        if amm == 3:
            x = set((val,)) ^ set(reverse_cards)
            return (3, [val] + sorted(x, reverse=True))
        else:
            return (2, reverse_cards)

    if len(cards) == 4:
        val, amm = cards.most_common()[0]
        x = set((val,)) ^ set(reverse_cards)
        return (1, [val] + sorted(x, reverse=True))

    if len(cards) == 5:
        # All cards are different so either straight or high card
        if straight:
            return (4, hc)
        else:
            return (0, reverse_cards)


def is_straight(hand):
    if len(hand) != 5:
        return False

    for i, x in enumerate(hand[:-1]):
        if x != hand[i+1] + 1:
            return False

    return True


@timer
def main():
    player_1_wins = 0
    for i, hand in enumerate(HANDS):
        a = hand[0]
        b = hand[1]
        hv_a = hand_value(a)
        hv_b = hand_value(b)
        if hv_a > hv_b:
            print(a, end=":  ")
            print(hv_a)
            print("A BEATS B")
            print(b, end=":  ")
            print(hv_b)
            player_1_wins += 1
        else:
            print(b, end=":  ")
            print(hv_b)
            print("B BEATS A")
            print(a, end=":  ")
            print(hv_a)

        print("===== {0} =====".format(i+1))


    return player_1_wins


if __name__ == '__main__':
    print(main())
