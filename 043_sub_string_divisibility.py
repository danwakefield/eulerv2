#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also has a
rather interesting sub-string divisibility property. Let d_1 be the 1st digit,
d_2 be the 2nd digit, and so on. In this way, we note the following:
    d_2 d_3 d_4 = 406 is divisible by 2
    d_3 d_4 d_5 = 063 is divisible by 3
    d_4 d_5 d_6 = 635 is divisible by 5
    d_5 d_6 d_7 = 357 is divisible by 7
    d_6 d_7 d_8 = 572 is divisible by 11
    d_7 d_8 d_9 = 728 is divisible by 13
    d_8 d_9 d_10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this
property.

Answer: 16695334890
"""
from __future__ import print_function
from utils import timer
from itertools import permutations
from functools import reduce


ANSWER = 16695334890


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


PRIMES = (17, 13, 11, 7, 5, 3, 2)


@timer
def main():
    matching = set()

    for n in permutations('0123456789', 10):
        if n[0] == '0':
            continue
        if n[5] != '0' and n[5] != '5':
            continue
        n = ''.join(n)

        for i, p in enumerate(PRIMES):
            s = n[7-i:10-i]
            if int(s) % p:
                break
        else:
            matching.add(int(n))

    return sum(matching)


if __name__ == '__main__':
    print(main())
