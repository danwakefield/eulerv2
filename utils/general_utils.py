import itertools


def take_n(n, gen):
    """Take the first N elements from a generator."""
    for _ in range(n):
        y = next(gen)
        yield y


def take_between(low, high, gen):
    for y in take_upto(high, take_from(low, gen)):
        yield y


def take_from(low, gen):
    for y in itertools.dropwhile(lambda x: x < low, gen):
        yield y


def take_upto(high, gen):
    for y in itertools.takewhile(lambda x: x <= high, gen):
        yield y
