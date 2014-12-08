#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=41

We shall say that an n -digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime. What is the largest n -digit pandigital
prime that exists?

Answer: 7652413
"""
from __future__ import print_function
from utils import timer, is_prime
from itertools import permutations


@timer
def main():
    # A prime n > 10 must end in one of these numbers.
    possible_prime_suffix = set(('1', '3', '7', '9'))
    highest_prime = 0

    # Progressivly create a smaller string of candidate numbers by
    # slicing the base str.
    str_num_base = '123456789'
    for x in range(9, 0, -1):
        str_num = str_num_base[:x]
        # Skip suffixes that are greater than the slice index, This stops
        # use getting possible values like 1239 which clearly isnt pandigital
        for suf in possible_prime_suffix:
            if int(suf) > x:
                continue
            # Remove the suffix from the number.
            suffed_str_num = str_num.replace(suf, '')
            # Get permutations of the remaining digits.
            # Append the suffix and check if the result is prime.
            for perm in permutations(suffed_str_num, x-1):
                i = int(''.join(perm) + suf)
                if is_prime(i):
                    # Store the prime but continue for the same iteration of x
                    # since its possible that smaller prime was given back from
                    # permutations first.
                    if i > highest_prime:
                        highest_prime = i
        # If a prime has been discovered this iteration of x highest
        # prime will not be 0 so return it.
        if highest_prime != 0:
            return highest_prime


if __name__ == '__main__':
    print(main())
