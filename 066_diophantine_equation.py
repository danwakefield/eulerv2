#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=66

Consider quadratic Diophantine equations of the form:
    x^2 – Dy^2 = 1
For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
It can be assumed that there are no solutions in positive integers when
D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:
    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
from __future__ import print_function
from utils import timer, is_perfect_square
from collections import OrderedDict


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


D = [x for x in range(1, 1001) if not is_perfect_square(x)]
X = OrderedDict(
    sorted(
        {x**2: x for x in range(1, 1000000)}.items(),
        key=lambda x: x[0]
    )
)


@timer
def main():
    # Invert the formula and used precomputed squares table for speedup.
    # As much as I wish that had worked, seems this is actually a very difficult
    # problem. Need to look at square root convergents and peels equations
    # to solve.
    results = {}

    for d in D:
        for y in X:
            dy = d*y + 1

            if dy in X:
                # print('{}^2 - {}x{}^2 = 1'.format(X[dy], d, yk))
                results[d] = X[dy]
                break
            else:
                s = is_perfect_square(dy)
                if s:
                    results[d] = s[0]
                    break

    largest = 0
    large_d = 0
    for k, v in results.items():
        if v > largest:
            large_d = k
            largest = v
    return large_d

if __name__ == '__main__':
    print(main())
