#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=33

The fraction^49 /_98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that^49 /_98 =^4 /_8 , which is correct, is obtained by cancelling
the 9s. We shall consider fractions like,^30 /_50 =^3 /_5 , to be
trivial examples. There are exactly four non-trivial examples of this
type of fraction, less than one in value, and containing two digits in
the numerator and denominator. If the product of these four fractions
is given in its lowest common terms, find the value of the
denominator.
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
