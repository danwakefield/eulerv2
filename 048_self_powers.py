#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317. Find the
last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 .

Answer: 9110846700
"""
from __future__ import print_function
from utils import timer


@timer
def main():
    total = 0
    for x in range(1, 1001):
        total += x**x

    return str(total)[-10:]


if __name__ == '__main__':
    print(main())
