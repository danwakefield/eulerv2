#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000 ?

Answer: 1366
"""
from __future__ import print_function
from utils import timer

def digit_sum(n):
    str_n = str(n)
    total = 0

    for x in str_n:
        total += int(x)

    return total

@timer
def main():
    return(digit_sum(2**1000))


if __name__ == '__main__':
    print(main())
