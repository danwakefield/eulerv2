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
from utils import timer
from math import factorial
power_digit_sum = __import__('016_power_digit_sum')

digit_sum = power_digit_sum.digit_sum

@timer
def main():
    return digit_sum(factorial(100))


if __name__ == '__main__':
    print(main())
