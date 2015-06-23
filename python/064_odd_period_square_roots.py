#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=64

All square roots are periodic when written as continued fractions and
can be written in the form:
    SEE URL, COMPLEX MATH TEMPLATING
"""
from __future__ import print_function
from utils import timer, take_n, square_numbers_gen
from collections import OrderedDict


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


SQUARES = OrderedDict()
for k in range(1, 12000):
    SQUARES[k] = k*k


@timer
def main():
    results = {}
    for d in range(1001):
        for x in SQUARES:
            for y in SQUARES:
                t = SQUARES[x] - (d*SQUARES[y])
                if t < 0:
                    break

                if t == 1:
                    results[d] = (x, y)
                    break
            if t == 1:
                break

    highest = 0
    highest_d = 0
    for k, v in results:
        if v[0] > highest:
            highest = v[0]
            highest_d = k

    return highest_d

if __name__ == '__main__':
    print(main())
