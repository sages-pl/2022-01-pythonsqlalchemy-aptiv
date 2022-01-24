"""
* Assignment: OOP Composition Composition
* Complexity: easy
* Lines of code: 10 lines
* Time: 3 min

English:
    1. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    2. Use composition
    3. Assignment demonstrates syntax, so do not add any attributes and methods (only type annotations)
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    2. Użyj kompozycji
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod (tylko anotacje typów)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Habitat)
    >>> assert isclass(Astronaut)
    >>> assert isclass(Rocket)
    >>> assert isclass(MarsMission)
    >>> assert MarsMission.__annotations__['habitat'] is Habitat
    >>> assert MarsMission.__annotations__['astronaut'] is Astronaut
    >>> assert MarsMission.__annotations__['rocket'] is Rocket
"""


