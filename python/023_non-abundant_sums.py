#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number. A number n is called deficient if the sum of its
proper divisors is less than n and it is called abundant if this sum
exceeds n . As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 =
16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less than this
limit. Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.

Answer: 4179871
"""
from __future__ import print_function
from utils import timer, factor_sum


ANSWER = 4179871


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    x_set = set(range(1, 28123))
    abundant = set()

    for n in x_set:
        if factor_sum(n) > n:
            abundant.add(n)

    abundant = list(abundant)
    abundant_sums = {}
    for i, n in enumerate(abundant):
        for k in abundant[i:]:
            s = k + n
            if s > 28123:
                break
            abundant_sums[s] = True

    return sum(x_set - abundant_sums.keys())


if __name__ == '__main__':
    print(main())
