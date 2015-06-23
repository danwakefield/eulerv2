#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find
the sum of all numbers which are equal to the sum of the factorial of
their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not
included.

Answer: 40730
"""
from __future__ import print_function
from utils import timer, composing_digits
from math import factorial


ANSWER = 40730


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


def digit_factorial_sum(n):
    return sum(factorial(x) for x in composing_digits(n))


@timer
def main():
    total = 0
    for n in range(3, 300000):
        dfs = digit_factorial_sum(n)
        if dfs == n:
            total += n

    return total


if __name__ == '__main__':
    print(main())
