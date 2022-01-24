
def km_to_meters(kilometers):
    """
    >>> km_to_meters(1)
    1000.0
    >>> km_to_meters(0)
    0.0
    >>> km_to_meters(-1)
    Traceback (most recent call last):
    ValueError: Argument must be not negative
    >>> km_to_meters([1, 2])
    Traceback (most recent call last):
    TypeError: Invalid argument type
    >>> km_to_meters('one')
    Traceback (most recent call last):
    TypeError: Invalid argument type
    >>> km_to_meters(1.5)
    1500.0
    >>> km_to_meters(True)
    Traceback (most recent call last):
    TypeError: Invalid argument type
    """
    if type(kilometers) not in {int, float}:
        raise TypeError('Invalid argument type')

    if kilometers < 0:
        raise ValueError('Argument must be not negative')

    return float(kilometers * 1000)
