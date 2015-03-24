#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:
    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation,^5 C_3 = 10.
In general,^n C_r = n!r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1,
and 0! = 1. It is not until n = 23,
that a value exceeds one-million:
    ^23 C_10 = 1144066.
How many, not necessarily distinct, values of ^n C_r, for 1 ≤ n ≤ 100,
are greater than one-million?

Answer: 4075
"""
from __future__ import print_function
from utils import timer, MILL
from math import factorial
from functools import lru_cache


ANSWER = 4075


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@lru_cache(maxsize=110)
def cached_fact(n):
    return factorial(n)


@timer
def main():
    total = 0
    for n in range(0, 101):
        for r in range(1, n+1):
            if (cached_fact(n) / (cached_fact(r) * cached_fact(n-r))) >= MILL:
                total += 1

    return total


if __name__ == '__main__':
    print(main())
