#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set
of four primes with this property. Find the lowest sum for a set of
five primes for which any two primes concatenate to produce another
prime.

Answer:
"""
from __future__ import print_function
from utils import timer, primes, take_n, is_prime
import itertools


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


PRIMES = list(take_n(1000, primes()))


@timer
def main():
    pass


if __name__ == '__main__':
    print(main())
