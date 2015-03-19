#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
prime factor of the number 600851475143 ?

Answer: 6857
"""
from __future__ import print_function
from utils import prime_factor, timer


ANSWER = 6857


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main(number=600851475143):
    return prime_factor(number)


if __name__ == '__main__':
    print(main())
