from __future__ import print_function
from time import time


def timer(func):
    """Timing decorator to check execution time of a routine"""
    def wrapper(*a, **kw):
        start = time()
        r = func(*a, **kw)
        duration = time() - start

        print('{0}: {1:.4f}s'.format(func.__name__, duration))
        return r

    return wrapper
