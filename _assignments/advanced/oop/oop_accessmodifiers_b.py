"""
* Assignment: OOP Access Init
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Modify class `Iris` to add attributes:
        a. Protected attributes: `sepal_length, sepal_width`
        b. Private attributes: `petal_length, petal_width`
        c. Public attribute: `species`
    2. Do not use `dataclass`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris` aby dodać atrybuty:
        a. Chronione atrybuty: `sepal_length, sepal_width`
        b. Private attributes: `petal_length, petal_width`
        c. Publiczne atrybuty: `species`
    2. Nie używaj `dataclass`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Iris)

    >>> result = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> assert hasattr(result, '_sepal_width')
    >>> assert hasattr(result, '_sepal_length')
    >>> assert hasattr(result, '_Iris__petal_width')
    >>> assert hasattr(result, '_Iris__petal_length')
    >>> assert hasattr(result, 'species')
"""


class Iris:
    pass


