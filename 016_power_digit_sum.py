#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000 ?

Answer: 1366
"""
from __future__ import print_function
from utils import timer, composing_digits


ANSWER = 1366


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    return sum(composing_digits(2**1000))


if __name__ == '__main__':
    print(main())
