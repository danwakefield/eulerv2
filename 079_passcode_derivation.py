#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=79

A common security method used for online banking is to ask the user
for three random characters from a passcode. For example, if the
passcode was 531278, they may ask for the 2nd, 3rd, and 5th
characters; the expected reply would be: 317. The text file,
keylog.txt , contains fifty successful login attempts. Given that the
three characters are always asked for in order, analyse the file so as
to determine the shortest possible secret passcode of unknown length.
"""
from __future__ import print_function
from utils import timer


ANSWER = 73162890


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


with open('./data/079_passcode_derivation.txt', 'r') as f:
    DATA = [x.strip('\n') for x in f.readlines()]


@timer
def main():
    digits = {}
    # We are doing a very cimple check.
    # We are going through all of the codes an counting
    # how many times digits appear before it.
    #
    # This would not work if the passcode had repeated digits
    # but it doesnt.
    # The idea is that for a passcode, ABC
    # B adds A to it before set and C add A and B to its set.
    # At the end we would see that A never appeared after anything
    # so must be the first character. B only appeared after A and
    # so forth
    for code in DATA:
        char = code[0]
        if char not in digits:
            digits[char] = set()

        char = code[1]
        if char not in digits:
            digits[char] = set()
        digits[char].add(x[0])

        char = code[2]
        if char not in digits:
            digits[char] = set()
        digits[char].add(x[0])
        digits[char].add(x[1])

    passcode = [None] * len(digits)
    for k, v in digits.items():
        passcode[len(v)] = k

    return int(''.join(passcode))

if __name__ == '__main__':
    print(main())
