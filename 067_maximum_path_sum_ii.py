#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
3 7 4 2 4 6 8 5 9 3 That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt,
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.

It is not possible to try every route to solve this problem, as
there are 2^99 altogether! If you could check one trillion (10^12 )
routes every second it would take over twenty billion years to check
them all. There is an efficient algorithm to solve it. ;o)
"""
from __future__ import print_function
from utils import timer


ANSWER = 7273


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


with open('./data/067_maximum_path_sum_ii.txt', 'r') as f:
    DATA = [x.strip().split() for x in f.readlines()]


def max_path_sum_in_triangle(t):
    '''
    walks the high values up the triangle by adding the highest of the
    two values in the cells to below_left and below_right to the current
    cell.
    I.E
        1
       2 3
    would become
        4
       2 3

    returns the value left at the top of the triangle
    '''
    triangle_height = len(t)

    for n in range(triangle_height - 2, -1, -1):
        for x in range(len(t[n])):
            below_left = int(t[n+1][x])
            below_right = int(t[n+1][x+1])

            t[n][x] = int(t[n][x]) + max((below_left, below_right))

    return t[0][0]


@timer
def main():
    return max_path_sum_in_triangle(DATA)


if __name__ == '__main__':
    print(main())
