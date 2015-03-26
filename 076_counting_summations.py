#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=76

It is possible to write five as a sum in exactly six different ways:
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two
positive integers?
"""
from __future__ import print_function
from utils import timer


ANSWER = 190569291


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    # Same solution as Q31 - Coin Sums, Combinatorics.
    # Only difference was to exclude 100 from candidates as one of the
    # conditions is 'sum of at least two .. Integers'
    target = 100
    cands = list(range(1, 100))
    ways = [1] + [0] * target

    for c in cands:
        for i in range(c, target+1):
            ways[i] += ways[i-c]

    return ways[-1]

if __name__ == '__main__':
    print(main())
