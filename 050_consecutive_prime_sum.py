#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred. The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953. Which prime, below
one-million, can be written as the sum of the most consecutive primes?
"""
from __future__ import print_function
from utils import timer, MILL, take_upto, primes


ANSWER = 997651


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


PRIMES = list(take_upto(MILL, primes()))
PRIME_SET = set(PRIMES)
PRIME_SUMS = [PRIMES[0]]

# Calculate the cumaltive sum of primes for each step.
for psi, p in enumerate(PRIMES[1:]):
    PRIME_SUMS.append(PRIME_SUMS[psi] + p)


@timer
def main():
    # We use a sliding window to calculate the longest run and its associated
    # prime.
    psl = len(PRIME_SUMS)
    high_run = 0
    high_prime = 0
    return 0

    for x in range(psl):
        if psl - x < high_run:
            print('break AAAA')
            break

        for y in range(psl - 1, x, -1):
            diff = PRIME_SUMS[y] - PRIME_SUMS[x]
            if diff > MILL:
                continue

            run_length = abs(x - y)
            if run_length < high_run:
                print('break BBBB')
                break

            if diff < high_prime:
                print('break CCCC')
                break

            if diff in PRIME_SET:
                if diff > high_prime:
                    print('high_run:{} high_prime:{}'.format(run_length, diff))
                    high_prime = diff
                    high_run = run_length

    return high_prime


if __name__ == '__main__':
    print(main())
