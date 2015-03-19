#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c ,
for which, a^2 + b^2 = c^2 For example, 3^2 + 4^2 = 9 + 16 = 25 =
5^2 . There exists exactly one Pythagorean triplet for which a + b +
c = 1000. Find the product abc .

Answer: a = 200, b = 375, c = 425,  product = 31875000
"""
from __future__ import print_function
from utils import timer


ANSWER = 31875000


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    for a in range(1, 1000):
        for b in range(a+1, 1000 - a):
            c = 1000 - a - b

            if c < b:
                break

            if (a**2 + b**2) == c**2:
                print('a: {}, b: {}, c: {}'.format(a, b, c))
                return a * b * c


if __name__ == '__main__':
    print(main())
