#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is
the smallest cube which has exactly three permutations of its digits
which are also cube. Find the smallest cube for which exactly five
permutations of its digits are cube.
"""
from __future__ import print_function
from utils import timer


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


def composing_digits_key(n):
    # We want an iummutable key for each number. If it is a permuation
    # then a sorted tuple of the digits will match.
    return tuple(sorted(x for x in str(n)))


def cubes_gen():
    x = 345
    while True:
        yield x**3
        x += 1


@timer
def main():
    d = {}

    for c in cubes_gen():
        k = composing_digits_key(c)
        if k not in d:
            d[k] = []

        d[k].append(c)
        if len(d[k]) == 5:
            return min(d[k])


if __name__ == '__main__':
    print(main())
