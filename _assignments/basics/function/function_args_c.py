"""
* Assignment: Function Arguments Power
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `power`
    2. Function takes two arguments
    3. Second argument is optional
    4. Function returns power of the first argument to the second
    5. If only one argument was passed, consider second equal to the first one
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `power`
    2. Funkcja przyjmuje dwa argumenty
    3. Drugi argument jest opcjonalny
    4. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    5. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(power)
    True
    >>> power(4, 3)
    64
    >>> power(3)
    27
"""


