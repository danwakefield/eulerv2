#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and
the square of the sum is 3025 − 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural
numbers and the square of the sum.

Answer: 25164150
"""
from __future__ import print_function
from utils import timer
import itertools


ANSWER = 25164150


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


def sum_squares(n):
    '''
    Not copied. how the hell did I manage an optimization like this??

    Takes advantage of the fact that y^2 = y+x+x^2 where y > 4
    I.e

    4 * 4 = 16
    5 * 5 = 25  ==  4 + 5 + 16

    Hard code the first few squares which dont share this behaviour

    Time Trial: n = 10100000: 1.097s
    '''
    s = [0, 1, 4, 9, 16]
    t = sum(s)
    last_square = 16
    last_pow = 4

    for x in range(5, n + 1):
        j = last_square + x + last_pow
        last_square = j
        last_pow = x
        t += j

    return t


def bar(n):
    '''
    Time Trial: n = 10100000: 3.170s
    '''
    return sum(x**2 for x in range(1, n + 1))


@timer
def main(n=100):
    sum_square = sum_squares(n)
    square_sum = pow(sum(range(n+1)), 2)

    return abs(sum_square - square_sum)


if __name__ == '__main__':
    print(main())
