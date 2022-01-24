"""
* Assignment: Mapping Define Dict
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `result: dict` representing input data
    2. Non-functional requirements:
        a. Assignmnet verifies creation of `dict()`
        b. Do not parse `DATA`, simply model `result` based on `DATA`
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or
           any other control-flow statement
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: dict` reprezentujący dane wejściowe
    2. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `dict()`
        b. Nie parsuj `DATA`, po prostu zamodeluj `result` bazując na `DATA`
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub
           jakiejkolwiek innej instrukcji sterującej
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert 'First Name' in result.keys(), \
    'Value `First Name` is not in the result keys'

    >>> assert 'Last Name' in result.keys(), \
    'Value `Last Name` is not in the result keys'

    >>> assert 'Missions' in result.keys(), \
    'Value `Missions` is not in the result keys'

    >>> assert 'Mark' in result['First Name'], \
    'Value `Mark` is not in the result values'

    >>> assert 'Watney' in result['Last Name'], \
    'Value `Watney` is not in the result values'

    >>> assert 'Ares1' in result['Missions'], \
    'Value `Ares1` is not in the result values'

    >>> assert 'Ares3' in result['Missions'], \
    'Value `Ares3` is not in the result values'
"""

DATA = """
    First Name: Mark
    Last Name: Watney
    Missions: Ares1, Ares3
"""

# dict[str,str|list]: with First Name, Last Name and Missions as keys
result = ...

