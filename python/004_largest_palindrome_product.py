#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99. Find
the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""
from __future__ import print_function
from utils import is_palindrome, timer


ANSWER = 906609


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    high = 0

    for x in range(1000, 100, -1):
        for y in range(x, 100, -1):
            t = x * y
            if is_palindrome(t):
                if t > high:
                    high = t

    return high


if __name__ == '__main__':
    print(main())
