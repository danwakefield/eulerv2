#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can
be written as the sum of fifth powers of their digits.

Answer: 443839
"""
from __future__ import print_function
from utils import timer


def composing_digits(n):
    return tuple(int(x) for x in str(n))

@timer
def main():
    n = 2
    total = 0
    while True:
        if n == sum(map(lambda x: x**5, composing_digits(n))):
            total += n
            if total > 400000:
                break

        n += 1

    return total

if __name__ == '__main__':
    print(main())
