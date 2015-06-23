#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001_2 (binary), is palindromic in
both bases. Find the sum of all numbers, less than one million, which
are palindromic in base 10 and base 2. (Please note that the
palindromic number, in either base, may not include leading zeros.)

Answer: 872187
"""
from __future__ import print_function
from utils import timer, is_palindrome, is_binary_palindrome, MILL


ANSWER = 872187


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    total = 0

    for n in range(MILL):
        if is_palindrome(n) and is_binary_palindrome(n):
            total += n

    return total


if __name__ == '__main__':
    print(main())
