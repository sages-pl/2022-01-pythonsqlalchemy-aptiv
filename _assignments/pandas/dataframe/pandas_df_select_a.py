"""
* Assignment: DataFrame Select
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    TODO: Translate to English
    X. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Przefiltruj `inplace` kolumnę 'petal_length' i pozostaw wartości powyżej 2.0
    3. Wyświetl 5 pierwszych wierszy
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
       sepal_length  sepal_width  petal_length  petal_width     species
    1           5.9          3.0           5.1          1.8   virginica
    2           6.0          3.4           4.5          1.6  versicolor
    3           7.3          2.9           6.3          1.8   virginica
    4           5.6          2.5           3.9          1.1  versicolor
    6           5.5          2.6           4.4          1.2  versicolor
"""
import pandas as pd


DATA = 'https://python.astrotech.io/_static/iris-clean.csv'

result = ...


