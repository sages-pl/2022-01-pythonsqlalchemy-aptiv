"""
* Assignment: Function Doctest Temperature
* Required: no
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Write implementation of a function `celsius_to_kelvin`
    2. Run doctests - all must succeed

Polish:
    1. Napisz implementację funkcji `celsius_to_kelvin`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(celsius_to_kelvin)
    True
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(1)
    274.15
    >>> celsius_to_kelvin(-1)
    272.15
    >>> celsius_to_kelvin('a')
    Traceback (most recent call last):
    TypeError: Invalid argument
    >>> celsius_to_kelvin([0, 1])
    [273.15, 274.15]
    >>> celsius_to_kelvin((0, 1))
    (273.15, 274.15)
    >>> celsius_to_kelvin({0, 1})
    {273.15, 274.15}
"""


