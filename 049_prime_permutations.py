#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another. There are no arithmetic sequences made up of three 1-,
2-, or 3-digit primes, exhibiting this property, but there is one
other 4-digit increasing sequence. What 12-digit number do you form by
concatenating the three terms in this sequence?

Answer: 296962999629
"""
from __future__ import print_function
from utils import timer, primes, is_permutation
from itertools import dropwhile, takewhile

primes_with_4_digits = list(takewhile(lambda x: x <= 9999,
                                      dropwhile(lambda x: x < 1000, primes())))


@timer
def main():
    for p1 in primes_with_4_digits:
        for p2 in primes_with_4_digits:
            if p2 <= p1:
                continue
            p3 = p2 + (p2 - p1)

            if p3 in primes_with_4_digits:
                if is_permutation(p1, p2) and is_permutation(p2, p3):
                    if p1 == 1487:
                        continue
                    return p1, p2, p3


if __name__ == '__main__':
    print(main())
