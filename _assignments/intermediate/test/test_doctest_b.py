"""
* Assignment: Function Doctest Distance
* Required: no
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    1. Write functions which convert distance given in kilometers to meters
    2. 1 km = 1000 m
    3. Distance cannot be negative
    4. Returned value must by float
    5. Write doctests
    6. Run doctests - all must succeed

Polish:
    1. Napisz funkcję, która przeliczy dystans podany w kilometrach na metry
    2. 1 km = 1000 m
    3. Dystans nie może być ujemny
    4. Zwracany dystans musi być float
    5. Napisz doctesty
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    1. Valid arguments:
        a. `int`
        b. `float`
    2. Invalid argument -> expect `TypeError`:
        a. `str`
        b. `list[int]`
        c. `list[float]`
        d. `bool`
        e. any other type
"""


def km_to_meters(kilometers):
    ...


