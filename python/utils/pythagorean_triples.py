"""
Utility generator for pythagorean triples using Euclid equations.

http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
"""
import itertools

from .number_sequences import factor_pairs


def pythag_triple_gen(n=3):
    """
    Yields pythagorean triples of (a,b,c) where (a^2 + b^2 = c^2)
    """
    for b in itertools.count(n):
        if b % 2:
            # Odd starting number.
            for m, n in factor_pairs(b):
                if m == n:
                    # Skip perfect square factors I.e 100 = 10*10
                    continue
                ms = m**2
                ns = n**2
                a = (ns - ms) // 2
                c = (ms + ns) // 2
                yield (a, b, c)
        else:
            for m, n in factor_pairs(b//2):
                if m == n:
                    continue
                ms = m**2
                ns = n**2
                a = (ns - ms)
                c = (ms + ns)
                yield (a, b, c)
