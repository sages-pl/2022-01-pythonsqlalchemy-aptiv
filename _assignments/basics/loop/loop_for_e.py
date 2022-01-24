"""
* Assignment: Loop For Translate
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define `result: str`
    2. Use `for` to iterate over `DATA`
    3. If letter is in `PL` then use conversion value as letter
    4. Add letter to `result`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list`
    2. Użyj `for` do iteracji po `DATA`
    3. Jeżeli litera jest w `PL` to użyj przekonwertowanej wartości jako litera
    4. Dodaj literę do `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'str'>

    >>> result
    'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

# str: DATA with substituted PL diacritic chars to ASCII letters
result = ...

