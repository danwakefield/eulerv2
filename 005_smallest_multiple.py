#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive
number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 232792560
"""
from __future__ import print_function
from utils import timer


ANSWER = 232792560


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    divisors = tuple(range(11, 21))

    # Incrementing 2520 means we exclude any candidates
    # that are divisable by 1-10 reducing the work we have to do.
    for x in range(2520, 99999999999, 2520):
        for d in divisors:
            if x % d != 0:
                break
        else:
            return x


if __name__ == '__main__':
    print(main())
