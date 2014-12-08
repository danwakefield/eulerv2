#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3. Find the sum of the only eleven
primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Answer: 748317
"""
from __future__ import print_function
from utils import timer, is_prime, primes
import itertools

def truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        right = int(str_n[:i+1])
        left = int(str_n[i:])
        if not is_prime(right) or not is_prime(left):
            return False

    return True


@timer
def main():
    trunc_count = 11
    trunc_primes = []

    for p in itertools.dropwhile(lambda x: x < 10, primes()):
        if truncatable_prime(p):
            trunc_count -= 1
            trunc_primes.append(p)
            if trunc_count == 0:
                break

    return trunc_primes, sum(trunc_primes)

if __name__ == '__main__':
    print(main())
