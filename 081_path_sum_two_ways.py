#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=81

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by only moving to the right and down , is indicated
in bold red and is equal to 2427. $$  \begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\  \color{red}{201} &
\color{red}{96} & \color{red}{342} & 965 & 150\\  630 & 803 &
\color{red}{746} & \color{red}{422} & 111\\  537 & 699 & 497 &
\color{red}{121} & 956\\  805 & 732 & 524 & \color{red}{37} &
\color{red}{331}  \end{pmatrix}  $$ Find the minimal path sum, in
matrix.txt (right click and "Save Link/Target As..."), a 31K text file
containing a 80 by 80 matrix, from the top left to the bottom right by
only moving right and down.
"""
from __future__ import print_function
from utils import timer


ANSWER = 427337

def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


with open('./data/081_path_sum_two_ways.txt', 'r') as f:
    DATA = f.readlines()
    DATA = [x.strip('\n').split(',') for x in DATA]


def minimal_path(r):
    size = len(r) - 1
    x_start = size

    # Walk from the bottom right to top left,
    # Compares the value of the current cell and
    # the one below / to the right and chooses the
    # minimal sum
    for y in range(size, -1, -1):
        for x in range(size, -1, -1):
            current = int(r[y][x])
            if y == size:
                below = None
            else:
                below = int(r[y+1][x])

            if x == size:
                right = None
            else:
                right = int(r[y][x+1])

            if below is None and right is None:
                continue

            if below is None:
                r[y][x] = current + right
                continue

            if right is None:
                r[y][x] = current + below
                continue

            if current + right < current + below:
                r[y][x] = current + right
            else:
                r[y][x] = current + below

    return r[0][0]


@timer
def main():
    return minimal_path(DATA)


if __name__ == '__main__':
    print(main())
