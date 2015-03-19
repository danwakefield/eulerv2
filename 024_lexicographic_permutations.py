#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012  021  102  120  201  210
What is the millionth lexicographic
permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
"""
from __future__ import print_function
from utils import timer, MILL
from itertools import permutations


ANSWER = 2783915460


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    digits = list(range(10))
    return int(''.join([str(x) for x in
                        sorted(permutations(digits))[MILL - 1]]))


if __name__ == '__main__':
    print(main())
