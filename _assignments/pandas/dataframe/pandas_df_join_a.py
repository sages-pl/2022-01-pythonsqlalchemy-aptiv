"""
* Assignment: DataFrame Join
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    TODO: Translate to English
    X. Run doctests - all must succeed

Polish:
    1. Na podstawie podanych URL:
        a. https://www.worldspaceflight.com/bios/eva/eva.php
        b. https://www.worldspaceflight.com/bios/eva/eva2.php
        c. https://www.worldspaceflight.com/bios/eva/eva3.php
        d. https://www.worldspaceflight.com/bios/eva/eva4.php
    2. Scrapuj stronę wykorzystując `pandas.read_html()`
    3. Połącz dane wykorzystując `pd.concat`
    4. Przygotuj plik `CSV` z danymi dotyczącymi spacerów kosmicznych
    5. Zapisz dane do pliku
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    # >>> assert result is not Ellipsis, \
    # 'Assign result to variable: `result`'
    # >>> assert type(result) is pd.DataFrame, \
    # 'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    Ellipsis

TODO: Doctests
"""

import pandas as pd


result = ...


