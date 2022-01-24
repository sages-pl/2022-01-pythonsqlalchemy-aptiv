"""
* Assignment: File Read Str
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read `FILE` to `result: str`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: str`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'hello'
"""

FILE = '_temporary.txt'
DATA = 'hello'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# str: FILE content
result = ...

