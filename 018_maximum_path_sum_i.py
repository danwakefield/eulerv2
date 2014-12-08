#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23. Find the maximum
total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE:
As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67 , is the same challenge
with a triangle containing one-hundred rows; it cannot be solved by
brute force, and requires a clever method! ;o)

Answer: 1074
"""
from __future__ import print_function
from utils import timer

TRIANGLE = [x.split() for x in
            '''
            75
            95 64
            17 47 82
            18 35 87 10
            20 04 82 47 65
            19 01 23 75 03 34
            88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
            41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
            70 11 33 28 77 73 17 78 39 68 17 57
            91 71 52 38 17 14 91 43 58 50 27 29 48
            63 66 04 68 89 53 67 30 73 16 69 87 40 31
            04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
            .split('\n')[1:]]

TEST_TRIANGLE = [x.split() for x in
                 '''
                 3
                 7 4
                 2 4 6
                 8 5 9 3'''
                 .split('\n')[1:]]

def max_path_sum_in_triangle(t):
    '''
    walks the high values up the triangle by adding the highest if the
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
    return max_path_sum_in_triangle(TRIANGLE)


if __name__ == '__main__':
    print(main())
