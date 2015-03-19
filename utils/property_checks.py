"""Property Checks for numbers and strings."""
import math


_SQUARE_BIT_PATTERNS = frozenset((0x00, 0x01, 0x04, 0x09, 0x10, 0x11,
                                  0x19, 0x21, 0x24, 0x29, 0x31, 0x39))


def is_perfect_square(n):
    """
    http://stackoverflow.com/q/295579
    """
    if n < 0:
        return False

    x = n & 0x3F
    if x not in _SQUARE_BIT_PATTERNS:
        return False

    sqrt = int(math.sqrt(n))

    return sqrt*sqrt == n


def is_permutation(a, b):
    return is_permutation_str(str(a), str(b))


def is_permutation_str(a, b):
    return sorted(a) == sorted(b)


def is_triangular_number(n):
    return is_perfect_square(8*n + 1)


def is_pentagonal_number(n):
    x = (((24*n + 1) ** 0.5) + 1) / 6
    return x == int(x)


def is_hexagonal_number(n):
    x = (((8*n + 1) ** 0.5) + 1) / 4
    return x == int(x)


def is_heptagonal_number(n):
    x = (((40*n + 9) ** 0.5) + 3) / 10
    return x == int(x)


def is_octagonal_number(n):
    x = (((3*n + 1) ** 0.5) + 1) / 3
    return x == int(x)


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def is_binary_palindrome(n):
    str_n = bin(n)[2:].lstrip('0')
    return str_n == str_n[::-1]


def _is_pandigital_closure():
    PANDIGITAL = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def is_pandigital(s, n):
        """
        Return False or None if not a palindrome true otherwise.

        None is returned if the number given has more digits than N.
        This allows anyone incrementing a counter to check that s will now
        never match and allow a loop break while still maintaining a false
        boolness if this isnt needed.
        """
        len_s = len(s)
        if len_s > n:
            return None
        elif len_s != n:
            return False

        for p in PANDIGITAL[:n]:
            if p not in s:
                return False

        return True
    return is_pandigital

is_pandigital = _is_pandigital_closure()
