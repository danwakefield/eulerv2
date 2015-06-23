#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as
an infinite continued fraction.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where the
number of digits in the numerator exceeds the number of digits in the
denominator. In the first one-thousand expansions, how many fractions
contain a numerator with more digits than denominator?

Answer: 153
"""
from __future__ import print_function
from utils import timer, composing_digits
from fractions import Fraction


ANSWER = 153


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


def mixed_num_to_improper_frac(x, frac):
    n = frac.numerator + x * frac.denominator
    return Fraction(n, frac.denominator)


def improper_frac_to_truncated_proper_frac(frac):
    # Tuned for this specific problem. x always == 1
    # and isnt needed since so dont calculate it
    # x = frac.numerator // frac.denominator
    r = frac.numerator % frac.denominator
    return Fraction(r, frac.denominator)


def invert_frac(frac):
    return Fraction(frac.denominator, frac.numerator)


@timer
def main():
    total = 0
    f = mixed_num_to_improper_frac(1, Fraction(1, 2))

    for i in range(2, 1001):
        # 3/2 => 1/2,  7/5 => 2/5
        f = improper_frac_to_truncated_proper_frac(f)
        # 2 + x/y =>  x+(2*y)/y
        x = mixed_num_to_improper_frac(2, f)
        # x/y => y/x
        x = invert_frac(x)
        f = mixed_num_to_improper_frac(1, x)

        numerator_digits = composing_digits(f.numerator)
        denominator_digits = composing_digits(f.denominator)
        if len(numerator_digits) > len(denominator_digits):
            total += 1
            print('Expansion {0:>3}: f = {1}'.format(i, f))

    return total


if __name__ == '__main__':
    print(main())
