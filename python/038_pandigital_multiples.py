#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:
    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4 and 5
giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""
from __future__ import print_function
from utils import timer
from itertools import permutations


ANSWER = 932718654


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    # The possible ways to split a nine digit number that so it
    # could fit the critera
    splits = [
        (1, 2, 3, 3),
        (2, 2, 2, 3),
        (2, 3, 4),
        (3, 3, 3),
        (4, 5),
    ]
    result = 0

    # They have already given us an example starting with 9 so anything
    # higher must also begin with one.
    # Cuts out a lot of useless checks.
    for p in (x for x in permutations('123456789', 9) if x[0] == '9'):

        p = ''.join(p)
        for split in splits:
            position = 0
            x = None

            for n, size in enumerate(split, 1):
                if x is None:
                    t = int(p[position:position+size]) / n
                    x = t
                else:
                    t = int(p[position:position+size]) / n
                    if t != x:
                        break
                position += size
            else:
                if int(p) > result:
                    result = int(p)

    return result


if __name__ == '__main__':
    print(main())
