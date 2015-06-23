#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=74

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:
    1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest
chain of numbers that link back to 169; it turns out that there are
only three such loops that exist:
    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop.
For example,
    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms,
but the longest non-repeating chain with a starting
number below one million is sixty terms. How many chains, with a
starting number below one million, contain exactly sixty non-repeating
terms?
"""
from __future__ import print_function
from utils import timer, composing_digits, MILL
from math import factorial
from functools import lru_cache


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


FACTS = {x: factorial(x) for x in range(0, 10)}


@lru_cache(maxsize=None)
def bar(x):
    return sum(FACTS[y] for y in composing_digits(x))


@timer
def main():
    total = 0
    import pudb; pudb.set_trace()  # XXX BREAKPOINT

    for i in range(68, 70):
        if i in (145, 169, 871, 872):
            continue
        k = i
        last = -1
        count = 0
        while True:
            k = bar(k)
            if k == last:
                break
            last = k
            count += 1

        print(count)

if __name__ == '__main__':
    print(main())
