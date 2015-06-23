#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=78

Let p(n) represent the number of different ways in which n coins can
be separated into piles. For example, five coins can separated into
piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O
Find the least value of n for which p(n) is divisible by one million.
"""
from __future__ import print_function
from utils import timer, ways, MILL


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    result = 3

    while True:
        result += 1
        x = ways(range(1, result+1), result)
        if x // MILL > 0:
            break

    return result

if __name__ == '__main__':
    print(main())
