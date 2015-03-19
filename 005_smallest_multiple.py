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

    for x in range(2520, 99999999999, 2520):
        if all(x % d == 0 for d in range(11, 21)):
            return x


if __name__ == '__main__':
    print(main())
