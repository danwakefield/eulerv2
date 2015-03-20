#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=51

By replacing the 1^st digit of the 2-digit number *3, it turns out
that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are
all prime. By replacing the 3^rd and 4^th digits of 56**3 with the
same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003,
56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
being the first member of this family, is the smallest prime with this
property. Find the smallest prime which, by replacing part of the
number (not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.
"""
from __future__ import print_function
from utils import timer


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()



@timer
def main():
    pass


if __name__ == '__main__':
    print(main())
