#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=20

n! means n × ( n − 1) × ... × 3 × 2 × 1 For example,
10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

Answer: 648
"""
from __future__ import print_function
from utils import timer, composing_digits
from math import factorial


ANSWER = 648


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    return sum(composing_digits(factorial(100)))


if __name__ == '__main__':
    print(main())
