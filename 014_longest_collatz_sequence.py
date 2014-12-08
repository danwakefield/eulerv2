#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive
integers:
    n → n /2 ( n is even)
    n → 3 n + 1 ( n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this
sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1. Which starting number, under
one million, produces the longest chain? NOTE: Once the chain starts
the terms are allowed to go above one million.

Answer: 837799
"""
from __future__ import print_function
from utils import timer


COLLATZ_CACHE = {}

def collatz(n, count=1):
    while n > 1:
        if n in COLLATZ_CACHE:
            count += COLLATZ_CACHE[n] - 1
            break

        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        count += 1

    return count

def cached_collatz(n):
    run_length = collatz(n)
    COLLATZ_CACHE[n] = run_length

    return run_length


@timer
def main():
    best_run = 0
    best_run_length = 0

    for n in range(1, 1000000):
        run_length = cached_collatz(n)

        if run_length > best_run_length:
            best_run_length = run_length
            best_run = n

    return best_run

if __name__ == '__main__':
    print(main())
