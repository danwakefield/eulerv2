#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:
 21 22 23 24 25
 20  7  8  9 10
 19  6  1  2 11
 18  5  4  3 12
 17 16 15 14 13
It can be verified that
the sum of the numbers on the diagonals is 101. What is the sum of the
numbers on the diagonals in a 1001 by 1001 spiral formed in the same
way?

Answer: 669171001
"""
from __future__ import print_function
from utils import timer

def square(n):
    '''
    turns the above square into the list
    [1, 3, 5, 7, 9, 13, 17, 21, 25]
    and returns the sum.

    Works for all n - O(n)
    '''
    sum_list = [1]
    square_length = n * n

    step_size = 2
    step_count = 0
    while sum_list[-1] < square_length:
        sum_list.append(sum_list[-1] + step_size)
        step_count += 1

        if step_count == 4:
            step_count = 0
            step_size += 2

    return sum(sum_list)


@timer
def main():
    return square(1001)
    pass


if __name__ == '__main__':
    print(main())
