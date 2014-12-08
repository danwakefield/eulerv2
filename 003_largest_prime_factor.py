#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
prime factor of the number 600851475143 ?

Answer: 6857
"""
from __future__ import print_function
from utils import prime_factor


def main(number=600851475143):
    return prime_factor(number)

if __name__ == '__main__':
    print(main())
