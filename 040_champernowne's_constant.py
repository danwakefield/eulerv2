#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the
positive integers: 0.123456789101112131415161718192021... It can be
seen that the 12^th digit of the fractional part is 1. If d_n
represents the n^th digit of the fractional part, find the value of
the following expression. d_1 × d_10 × d_100 × d_1000 × d_10000 ×
d_100000 × d_1000000

Answer: 210
"""
from __future__ import print_function
from utils import timer, digit_length, composing_digits
import itertools
import functools
import operator


@timer
def main():
    next_slice = 1
    total_digit_length = 0
    indexs = []

    for n in itertools.count(1):
        n_length = digit_length(n)

        if total_digit_length + n_length == next_slice:
            indexs.append((composing_digits(n)[-1], n))
            next_slice *= 10
            if next_slice > 1000000:
                break
        elif total_digit_length + n_length > next_slice:
            # offset is how many extra digits there are in n.
            # remove the extra and another 1 to compensate for 0 based index
            offset = (total_digit_length + n_length) - next_slice
            indexs.append((composing_digits(n)[n_length - offset - 1], n))
            next_slice *= 10
            if next_slice > 1000000:
                break

        total_digit_length += n_length

    return functools.reduce(lambda x, y: x*y[0], indexs, 1)


if __name__ == '__main__':
    print(main())
