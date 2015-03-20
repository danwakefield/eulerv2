#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order. Find the
smallest positive integer, x , such that 2 x , 3 x , 4 x , 5 x , and 6
x , contain the same digits.
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
