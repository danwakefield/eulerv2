#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=58

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.
        37 36 35 34 33 32 31
        38 17 16 15 14 13 30
        39 18  5  4  3 12 29
        40 19  6  1  2 11 28
        41 20  7  8  9 10 27
        42 21 22 23 24 25 26
        43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

Answer: 26241
"""
from __future__ import print_function
from utils import timer, is_prime


ANSWER = 26241


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


def percentage(a, b):
    return int((float(a) / b) * 100)


def diagonal_square_gen():
    """
    Generator for the corners of a integer spiral.

    Yielded values contain the length of the edge they exist on.
    """
    step_length = 2
    side_length = step_length + 1
    last = 1
    yield (1, 1)
    while True:
        for _ in range(4):
            last += step_length
            yield (last, side_length)

        step_length += 2
        side_length = step_length + 1


@timer
def main():
    corners = 1
    prime_corners = 0
    g = diagonal_square_gen()
    # Skip the centre 1 as it isnt prime resulting in an immediate exit
    next(g)
    for cnr, edge_len in g:
        corners += 1
        if is_prime(cnr):
            prime_corners += 1

        if percentage(prime_corners, corners) < 10:
            return edge_len


if __name__ == '__main__':
    print(main())
