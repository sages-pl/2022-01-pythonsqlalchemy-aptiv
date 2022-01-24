
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)


# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     if len(args) == 0:
# ...         return 0
# ...     return sum(args) / len(args)
# ...
# ... mean()
# 174 ns ± 29.2 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     try:
# ...         return sum(args) / len(args)
# ...     except ZeroDivisionError:
# ...         return 0
# ...
# ... mean()
# 395 ns ± 65.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)
