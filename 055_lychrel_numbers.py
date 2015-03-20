#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly.
For example,
    349 + 943 = 1292,
    1292 + 2921 = 4213
    4213 + 3124 = 7337
That is, 349 took three
iterations to arrive at a palindrome. Although no one has proved it
yet, it is thought that some numbers, like 196, never produce a
palindrome. A number that never forms a palindrome through the reverse
and add process is called a Lychrel number. Due to the theoretical
nature of these numbers, and for the purpose of this problem, we shall
assume that a number is Lychrel until proven otherwise. In addition
you are given that for every number below ten-thousand, it will either
(i) become a palindrome in less than fifty iterations, or, (ii) no
one, with all the computing power that exists, has managed so far to
map it to a palindrome. In fact, 10677 is the first number to be shown
to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits). Surprisingly,
there are palindromic numbers that are themselves Lychrel numbers; the
first example is 4994. How many Lychrel numbers are there below ten-
thousand? NOTE: Wording was modified slightly on 24 April 2007 to
emphasise the theoretical nature of Lychrel numbers.

Answer: 249
"""
from __future__ import print_function
from utils import timer, is_palindrome, TTHOU
from functools import lru_cache


ANSWER = 249


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@lru_cache(maxsize=None)
def is_lychrel(n, iterations=51):
    if iterations == 0:
        return True

    s = n + int(str(n)[::-1])
    if is_palindrome(str(s)):
        return False

    return is_lychrel(s, iterations-1)


@timer
def main():
    total = 0
    for i in range(1, TTHOU+1):
        if is_lychrel(i):
            total += 1

    return total


if __name__ == '__main__':
    print(main())
