#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes: 41
= 2 + 3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive
primes that adds to a prime below one-hundred. The longest sum of
consecutive primes below one-thousand that adds to a prime, contains
21 terms, and is equal to 953. Which prime, below one-million, can be
written as the sum of the most consecutive primes?
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
