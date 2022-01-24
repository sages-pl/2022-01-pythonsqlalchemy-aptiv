"""
* Assignment: Sequence GetItem Negative
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define `result_a: tuple` with row from `DATA` at index -5
    2. Define `result_b: tuple` with row from `DATA` at index -3
    3. Define `result_c: tuple` with row from `DATA` at index -1
    4. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result_a: tuple` z wierszem z `DATA` o indeksie -5
    2. Zdefiniuj `result_b: tuple` z wierszem z `DATA` o indeksie -3
    3. Zdefiniuj `result_c: tuple` z wierszem z `DATA` o indeksie -1
    4. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign result to variable: `result_c`'

    >>> assert type(result_a) is tuple, \
    'Variable `result_a` has invalid type, should be tuple'
    >>> assert type(result_b) is tuple, \
    'Variable `result_b` has invalid type, should be tuple'
    >>> assert type(result_c) is tuple, \
    'Variable `result_c` has invalid type, should be tuple'

    >>> assert len(result_a) == 5, \
    'Variable `result_a` length should be 5'
    >>> assert len(result_b) == 5, \
    'Variable `result_b` length should be 5'
    >>> assert len(result_c) == 5, \
    'Variable `result_c` length should be 5'

    >>> result_a
    (5.1, 3.5, 1.4, 0.2, 'setosa')

    >>> result_b
    (6.3, 2.9, 5.6, 1.8, 'virginica')

    >>> result_c
    (4.7, 3.2, 1.3, 0.2, 'setosa')
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# tuple[float|str]: row from `DATA` at index -5
result_a = ...

# tuple[float|str]: row from `DATA` at index -3
result_b = ...

# tuple[float|str]: row from `DATA` at index -1
result_c = ...

