#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some
research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone, Which has twenty-eight. And on leap years, twenty-nine.
A leap year occurs on any year evenly
divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

Answer: 171
"""
from __future__ import print_function
from utils import timer
import calendar


ANSWER = 171


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    sundays = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if calendar.monthrange(y, m)[0] == 6:
                sundays += 1

    return sundays


if __name__ == '__main__':
    print(main())
