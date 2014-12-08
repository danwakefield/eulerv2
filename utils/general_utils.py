

def take_n(n, gen):
    """Take the first N elements from a generator."""
    for _ in range(n):
        y = next(gen)
        yield y
