#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=65

    SEE URL, COMPLEX MATH TEMPLATING
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
