#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=68

Consider the following "magic" 3-gon ring, filled with the numbers 1
to 6, and each line adding to nine.
             4
              3
             1 2 6
            5
Working clockwise , and starting
from the group of three with the numerically lowest external node
(4,3,2 in this example), each solution can be described uniquely. For
example, the above solution can be described by the set:
    4,3,2; 6,2,1; 5,1,3
It is possible to complete the ring with four different totals:
    9, 10, 11, and 12.
There are eight solutions in total. Total Solution Set:
    9  4,2,3; 5,3,1; 6,1,2
    9  4,3,2; 6,2,1; 5,1,3
    10 2,3,5; 4,5,1; 6,1,3
    10 2,5,3; 6,3,1; 4,1,5
    11 1,4,6; 3,6,2; 5,2,4
    11 1,6,4; 5,4,2; 3,2,6
    12 1,5,6; 2,6,4; 3,4,5
    12 1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16 and 17 digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
from __future__ import print_function
from utils import timer
from itertools import permutations


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


# Bit confusing but these are the array indexes for each location on the Gon.
# It helps to look at the image on the question page.
ROWS = [
    [0, 1, 2],
    [3, 2, 4],
    [5, 4, 6],
    [7, 6, 8],
    [9, 8, 1],
]


def check(a):
    row_sum = 0
    # Requirement of the problem, If ten is in any of these positions the
    # string repr will be 17 digits not 16
    # Also eliminates loops, not sure if the branch overhead wins or
    # looses in this case though.
    if a[1] == 10 or a[2] == 10 or a[4] == 10 or a[6] == 10 or a[8] == 10:
        return False

    for r in ROWS:
        x = a[r[0]] + a[r[1]] + a[r[2]]
        if not row_sum:
            row_sum = x
        else:
            if row_sum != x:
                return False
    return True


CANDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@timer
def main():
    result = 0

    for x in filter(check, permutations(CANDS, len(CANDS))):
        n = []
        low_external = 20
        low_index = 10

        # This is for finding the 'numerically lowest external node'
        for i, r in enumerate(ROWS):
            if x[r[0]] < low_external:
                low_index = i
                low_external = x[r[0]]

        # This uses the index discovered in the last loop as the starting
        # point of the string repr of the Gon.
        for r in ROWS[low_index:] + ROWS[:low_index]:
            n.append(x[r[0]])
            n.append(x[r[1]])
            n.append(x[r[2]])

        # Ugly, Got to be a better way to do this.
        s = int(''.join(map(str, n)))
        if s > result:
            print(s)
            result = s
    return result

if __name__ == '__main__':
    print(main())
