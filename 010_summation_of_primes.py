#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of
all the primes below two million.

Answer: 142913828922
"""
from __future__ import print_function
from utils import timer, primes, MILL
from itertools import takewhile


@timer
def main(n=MILL*2):
    return sum(takewhile(lambda x: x < n, primes()))


if __name__ == '__main__':
    print(main())
