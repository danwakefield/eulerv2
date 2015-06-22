from __future__ import division
from .number_sequences import factors, _factor_pairs_v2
from math import log, factorial


def _rotate_digits_closure():
    LN10 = log(10)
    def rotate_digits(n):
        # http://jsperf.com/digit-rotation
        return (n // 10 >> 0) + (n % 10) * pow(10, int(log(n) / LN10))

    return rotate_digits

rotate_digits = _rotate_digits_closure()

def digit_length(n):
    # http://stackoverflow.com/a/1489873
    # Binary search is achieved by the nesting of the ifs.
    # only works on integers 0 to 1e10-1
    if n >= 10000:  # 1e4
        if n >= 10000000:  # 1e7
            if n >= 100000000:  # 1e8
                if n >= 1000000000:  # 1e9
                    return 10
                else:
                    return 9
            else:
                return 8
        elif n >= 100000:  # 1e5
            if n >= 1000000:  # 1e6
                return 7
            else:
                return 6
        else:
            return 5
    elif n >= 100:  # 1e2
        if n >= 1000:  # 1e3
            return 4
        else:
            return 3
    elif n >= 10:  # 1e1
        return 2
    else:
        return 1


def composing_digits(n):
    return tuple(int(x) for x in str(n))


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd_multiple(*a):
    a = list(a)

    while len(a) > 1:
        x = a.pop()
        y = a.pop()
        g = gcd(x, y)
        a.append(g)
    return a[0]


def factor_sum(n):
    d = {}
    for f in _factor_pairs_v2(n):
        d[f] = True

    del d[n]
    return sum(d.keys())


def central_binomial_coefficient(n):
    # (2n)!/(n!)^2
    return factorial(2*n) // factorial(n) ** 2


def prime_factor(n):
    sqrt = int(n ** 0.5)
    for x in range(2, sqrt + 1):
        while n % x == 0:
            n //= x

            if n == 1 or n == x:
                return x


def ways(cands, target):
    w = [1] + [0] * target

    for c in cands:
        for i in range(c, target+1):
            w[i] += w[i-c]

    return w[-1]
