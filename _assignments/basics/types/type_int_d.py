"""
* Assignment: Type Int Truediv
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Calculate altitude in kilometers:
        a. Kármán Line Earth: 100_000 m
        b. Kármán Line Mars: 80_000 m
        c. Kármán Line Venus: 250_000 m
    2. In Calculations use floordiv (`//`)
    3. Run doctests - all must succeed

Polish:
    1. Oblicz wysokości w kilometrach:
        a. Linia Kármána Ziemia: 100_000 m
        b. Linia Kármána Mars: 80_000 m
        c. Linia Kármána Wenus: 250_000 m
    2. W obliczeniach użyj floordiv (`//`)
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    * Kármán line (100 km) - boundary between planets's atmosphere and space

Hints:
    * 1 km = 1000 m

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert karman_line_earth is not Ellipsis, \
    'Assign result to variable: `karman_line_earth`'
    >>> assert karman_line_mars is not Ellipsis, \
    'Assign result to variable: `karman_line_mars`'
    >>> assert karman_line_venus is not Ellipsis, \
    'Assign result to variable: `karman_line_venus`'
    >>> assert type(karman_line_earth) is int, \
    'Variable `karman_line_earth` has invalid type, should be int'
    >>> assert type(karman_line_mars) is int, \
    'Variable `karman_line_mars` has invalid type, should be int'
    >>> assert type(karman_line_venus) is int, \
    'Variable `karman_line_venus` has invalid type, should be int'

    >>> karman_line_earth
    100
    >>> karman_line_mars
    80
    >>> karman_line_venus
    250
"""

m = 1
km = 1000 * m

# int: 100_000 meters in km
karman_line_earth = ...

# int: 80_000 meters in km
karman_line_mars = ...

# int: 250_000 meters in km
karman_line_venus = ...

