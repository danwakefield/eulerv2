#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length
sides, { a , b , c }, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50} For which value of p ≤ 1000, is the
number of solutions maximised?
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
