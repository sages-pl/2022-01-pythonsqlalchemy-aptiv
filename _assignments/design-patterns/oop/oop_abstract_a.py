"""
* Assignment: OOP Abstract Syntax
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Create abstract class `Iris`
    2. Create abstract method `get_name()` in `Iris`
    3. Create class `Setosa` inheriting from `Iris`
    4. Try to create instance of a class `Setosa`
    5. Try to create instance of a class `Iris`
    6. Run doctests - all must succeed

Polish:
    1. Stwórz klasę abstrakcyjną `Iris`
    2. Stwórz metodę abstrakcyjną `get_name()` w `Iris`
    3. Stwórz klasę `Setosa` dziedziczące po `Iris`
    4. Spróbuj stworzyć instancje klasy `Setosa`
    5. Spróbuj stworzyć instancję klasy `Iris`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract

    >>> assert isabstract(Iris), \
    'Iris class should be abstract, inherit from ABC or use metaclass=ABCMeta'

    >>> assert hasattr(Iris.get_name, '__isabstractmethod__'), \
    'Iris.get_name() method should be abstract, use @abstractmethod decorator'

    >>> assert not isabstract(Setosa), \
    'Setosa should not be abstract class'

    >>> assert not hasattr(Setosa.get_name, '__isabstractmethod__'), \
    'Setosa.get_name() should not be an abstract method'

    >>> iris = Iris()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Iris with abstract method get_name
    >>> setosa = Setosa()

Warning:
    * Last line of doctest, second to last word of `TypeError` message
    * In Python 3.7, 3.8 there is "methods" word in doctest
    * In Python 3.9 there is "method" word in doctest
    * So it differs by "s" at the end of "method" word
"""

