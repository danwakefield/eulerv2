#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order. Find the
smallest positive integer, x such that 2x, 3x, 4x, 5x, and 6x
contain the same digits.
"""
from __future__ import print_function
from utils import timer, composing_digits
import itertools


ANSWER = 142857


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


MULTS = (6, 5, 4, 3, 2)


def check(x, y):
    if sorted(composing_digits(x)) == sorted(composing_digits(y)):
        return True
    return False


@timer
def main():
    for i in itertools.count(1):
        for mult in MULTS:
            if not check(i, mult*i):
                break
        else:
            return i


if __name__ == '__main__':
    print(main())
