#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from __future__ import print_function
from utils import timer


ANSWER = 233168


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    return sum(x for x in range(1000) if not x % 3 or not x % 5)


if __name__ == '__main__':
    print(main())
