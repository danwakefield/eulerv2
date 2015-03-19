#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=32

We shall say that an n digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital. The product 7254 is unusual, as the
identity, 39 × 186 = 7254, containing multiplicand, multiplier, and
product is 1 through 9 pandigital. Find the sum of all products whose
multiplicand/multiplier/product identity can be written as a 1 through
9 pandigital. HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.

Answer: 45228
"""
from __future__ import print_function
from utils import timer, is_pandigital


ANSWER = 45228


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    products = set()

    for a in range(2, 3000):
        for b in range(2, 3000):
            p = a*b
            pand = is_pandigital(str(a) + str(b) + str(p), 9)

            if pand:
                products.add(p)
            elif pand is None:
                break

    return sum(products)


if __name__ == '__main__':
    print(main())
