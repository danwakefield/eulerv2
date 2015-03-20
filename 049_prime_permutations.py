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
from utils import timer, primes, is_permutation, take_between
from itertools import dropwhile, takewhile


ANSWER = 296962999629


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


PRIMES_WITH_4_DIGITS = list(take_between(1000, 9999, primes()))


@timer
def main():
    for p1 in PRIMES_WITH_4_DIGITS:
        for p2 in PRIMES_WITH_4_DIGITS:
            if p2 <= p1:
                continue
            p3 = p2 + (p2 - p1)

            if p3 in PRIMES_WITH_4_DIGITS:
                if is_permutation(p1, p2) and is_permutation(p2, p3):
                    if p1 == 1487:
                        continue
                    return int(str(p1) + str(p2) + str(p3))


if __name__ == '__main__':
    print(main())
