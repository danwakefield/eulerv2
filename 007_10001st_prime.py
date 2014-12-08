#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10 001st prime number?

Answer: 104743
"""
from __future__ import print_function
from utils import timer, primes
from itertools import islice


@timer
def main():
    return next(islice(primes(), 10000, 10001))


if __name__ == '__main__':
    print(main())
