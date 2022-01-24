"""
* Assignment: Mapping Generate Enumerate
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict`
    2. Assign to `result` converted `DATA` to `dict`
    3. Use `enumerate()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniu `result: dict`
    2. Przypisz do `result` przekonwertowane `DATA` do `dict`
    3. Użyj `enumerate()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`
    * `enumerate()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is int for x in result.keys()), \
    'All dict keys should be int'

    >>> assert all(type(x) is str for x in result.values()), \
    'All dict values should be str'

    >>> result
    {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
"""

DATA = ['setosa', 'versicolor', 'virginica']

# dict[int,str]: enumerated DATA to dict
result = ...

