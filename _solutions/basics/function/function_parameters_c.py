
def default(a, b=None):
    if b is None:
        b = a
    return {'a': a, 'b': b}
