#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=56

A googol (10^100 ) is a massive number: one followed by one-hundred
zeros; 100^100 is almost unimaginably large: one followed by two-
hundred zeros. Despite their size, the sum of the digits in each
number is only 1. Considering natural numbers of the form, a^b ,
where a, b < 100, what is the maximum digital sum?

Answer: 972
"""
from __future__ import print_function
from utils import timer, composing_digits


@timer
def main():
    highest_sum = 0
    for a in range(1, 100):
        for b in range(2, 100):
            s = sum(composing_digits(a**b))
            if s > highest_sum:
                highest_sum = s

    return highest_sum


if __name__ == '__main__':
    print(main())
