#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=63

The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an n'th power?
"""
from __future__ import print_function
from utils import timer, digit_length


ANSWER = 49


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    total = 0

    for p in range(1, 400):
        for i in range(1, 1000):
            x = len(str(i ** p))
            if x == p:
                total += 1
            if x > p:
                break

    return total


if __name__ == '__main__':
    print(main())
