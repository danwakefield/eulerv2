#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=77

It is possible to write ten as the sum of primes in exactly five
different ways:
    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in
over five thousand different ways?
"""
from __future__ import print_function
from utils import timer, ways, take_upto, primes


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    result = 0
    while True:
        result += 1
        x = ways(take_upto(result, primes()), result)
        if x > 5000:
            break
    return result


if __name__ == '__main__':
    print(main())
