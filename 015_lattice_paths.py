#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner. How many such routes are there through a 20×20 grid?

Answer: 137846528820
"""
from __future__ import print_function
from utils import timer, central_binomial_coefficient
from math import factorial

# Paths through a lattice can be described using
# 'central binomial coefficents'
#
# Examples here:
# http://www.robertdickau.com/manhattan.html

@timer
def main():
    return central_binomial_coefficient(20)


if __name__ == '__main__':
    print(main())
