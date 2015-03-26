#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=71

Consider the fraction, n/d , where n and d are positive integers.
If n < d and HCF(n, d)=1, it is called a reduced proper fraction. If we
list the set of reduced proper fractions for d ≤ 8 in ascending order
of size, we get:
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
    4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the
left of 3/7.
"""
from __future__ import print_function
from utils import timer, MILL
from fractions import Fraction
import itertools


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


LIMIT = 8


def coprime_gen(m, n):
    d = {Fraction(n, m): {}}

    yield Fraction(2*cm - cn, cm)

    yield Fraction(2*cm + cn, cm)

    yield Fraction(cm + 2*cn, cn)


@timer
def main():
    rpf = set()
    import pudb; pudb.set_trace()  # XXX BREAKPOINT

    for x in coprime_gen(2, 1):
        rpf.add(x)



if __name__ == '__main__':
    print(main())
