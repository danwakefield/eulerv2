#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=82

NOTE: This problem is a more challenging version of Problem 81 . The
minimal path sum in the 5 by 5 matrix below, by starting in any cell
in the left column and finishing in any cell in the right column, and
only moving up, down, and right, is indicated in red and bold; the sum
is equal to 994.

| 131 | 673 |*234 |*103 |*18  |
|*201 |*96  |*342 | 965 | 150 |
| 630 | 803 | 746 | 422 | 111 |
| 537 | 699 | 497 | 121 | 956 |
| 805 | 732 | 524 | 37  | 331 |

Find the minimal path sum, in matrix.txt (right
click and "Save Link/Target As..."), a 31K text file containing a 80
by 80 matrix, from the left column to the right column.
"""
from __future__ import print_function
from utils import timer
import copy


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()

TEST_DATA = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


with open('./data/082_path_sum_three_ways.txt', 'r') as f:
    DATA = f.readlines()
    # zip flips the rows to columns since we want to operate on them
    DATA = list(reversed(list(zip(
        *[map(int, x.strip('\n').split(',')) for x in DATA]))))


def minimal_path(d):
    import pudb
    pudb.set_trace()

    best = list(copy.copy(d[0]))
    for i, col in enumerate(d[1:], 1):
        best[0] += int(col[0])
        for j, cell in enumerate(col[1:], 1):
            cell = int(cell)
            try:
                best[j] = min(cell + best[j-1], cell + int(d[i-1][j]))
            except IndexError:
                pass

        for j, cell in enumerate(col):
            cell = int(cell)
            try:
                best[j] = min(best[j], best[j+1] + int(d[i-1][j]))
            except IndexError:
                pass

    return min(d[-1])


@timer
def main():
    global TEST_DATA
    TEST_DATA = list(reversed(list(zip(*TEST_DATA))))
    return minimal_path(TEST_DATA)


if __name__ == '__main__':
    print(main())
