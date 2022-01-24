"""
* Assignment: OOP Interface Implement
* Complexity: easy
* Lines of code: 12 lines
* Time: 5 min

English:
    1. Define class `Setosa` implementing `IrisInterface`
    2. Implement interface
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Setosa` implementującą `IrisInterface`
    2. Zaimplementuj interfejs
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(self).values()`
    * `mean = sum() / len()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert issubclass(Setosa, IrisInterface)
    >>> assert hasattr(Setosa, 'mean')
    >>> assert hasattr(Setosa, 'sum')
    >>> assert hasattr(Setosa, 'len')

    >>> assert isfunction(Setosa.mean)
    >>> assert isfunction(Setosa.sum)
    >>> assert isfunction(Setosa.len)

    >>> Setosa.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> setosa = Setosa(5.1, 3.5, 1.4, 0.2)
    >>> setosa.len()
    4
    >>> setosa.sum()
    10.2
    >>> setosa.mean()
    2.55
"""

class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def sum(self) -> float:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError


