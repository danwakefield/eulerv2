#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square. 9 = 7 + 2×1
^2 15 = 7 + 2×2^2 21 = 3 + 2×3^2 25 = 7 + 2×3^2 27 = 19 + 2×2^2 33
= 31 + 2×1^2 It turns out that the conjecture was false. What is the
smallest odd composite that cannot be written as the sum of a prime
and twice a square?

Answer: 65537
"""
from __future__ import print_function
from utils import timer, primes
import itertools


ANSWER = 65537


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


primes_l = set(itertools.islice(primes(), 10000))
square_sums = [2*(x**2) for x in range(40)]


@timer
def main():
    for n in itertools.count(3, 2):
        for p in primes_l:
            if p > n:
                break
            for s in square_sums:
                t = p + s
                if t == n:
                    break
            else:
                return n


if __name__ == '__main__':
    print(main())
