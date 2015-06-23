#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:
    n ² + n + 41
It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1)
+ 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
clearly divisible by 41. The incredible formula
    n ² − 79 n + 1601
was discovered, which produces 80 primes for the consecutive values
n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n ² + an + b
    where | a | < 1000 and | b | < 1000

    where | n | is the modulus/absolute value of n
    e.g.
    |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b ,
for the quadratic expression that produces the maximum number of
primes for consecutive values of n , starting with n = 0.

b has to be prime since when n is 0
0**2 + 0 * a + b

Answer: -59231
"""
from __future__ import print_function
from utils import timer, primes, is_prime
from itertools import takewhile


ANSWER = -59231


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    primes_less_1000 = list(takewhile(lambda x: x < 1000, primes()))
    highest = [0, 0, 0]

    for a in range(-999, 1001):
        for b in primes_less_1000:
            n = 0
            while is_prime((n**2) + (a*n) + b):
                n += 1

            if n > highest[0]:
                highest[0] = n
                highest[1] = a
                highest[2] = b

    print(highest)
    return highest[1] * highest[2]


if __name__ == '__main__':
    print(main())
