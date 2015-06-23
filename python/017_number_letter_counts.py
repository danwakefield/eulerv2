#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If
all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used? NOTE: Do not count
spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance
with British usage.

Answer: 21124
"""
from __future__ import print_function
from utils import timer


ANSWER = 21124


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


MAPS = {
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),
    20: len('twenty'),
    30: len('thirty'),
    40: len('forty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('ninety'),
}


def length_of_number_as_string(n):
    if n > 1000:
        raise NotImplementedError('Only handles upto 1000')

    # lru_cache would be a good idea here
    length = 0
    quot, remainder = divmod(n, 100)
    if quot:
        if quot == 10:
            return len('onethousand')

        length += MAPS[quot]
        length += 7  # hundred
        if remainder:
            length += 3  # and

    if remainder:
        if remainder <= 20:
            length += MAPS[remainder]
        else:
            tens = (remainder // 10) * 10
            remainder = remainder % 10
            length += MAPS[tens]
            if remainder:
                length += MAPS[remainder]

    return length


@timer
def main():
    total = 0
    for n in range(1, 1001):
        total += length_of_number_as_string(n)

    return total


if __name__ == '__main__':
    print(main())
