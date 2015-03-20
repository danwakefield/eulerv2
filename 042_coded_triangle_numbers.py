#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=42

The n^th term of the sequence of triangle numbers is given by,
    t_n = ½n(n+1)
so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a
number corresponding to its alphabetical position and adding these
values we form a word value. For example, the word value for SKY is 19
+ 11 + 25 = 55 = t_10 . If the word value is a triangle number then
we shall call the word a triangle word. Using words.txt (right click
and 'Save Link/Target As...'), a 16K text file containing nearly two-
thousand common English words, how many are triangle words?

Answer: 162
"""
from __future__ import print_function
from utils import timer, word_score, is_triangular_number


ANSWER = 162


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


with open('./data/042_coded_triangle_numbers.txt', 'r') as f:
    DATA = f.readlines()
    DATA = DATA[0].replace('"', '').split(',')


@timer
def main():
    total = 0

    for word in DATA:
        if is_triangular_number(word_score(word)):
            total += 1

    return total

if __name__ == '__main__':
    print(main())
