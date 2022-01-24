"""
* Assignment: Loop For Counter
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Iterate over `DATA`
    2. Count occurrences of each number
    3. Create empty `result: dict[int, int]`:
        a. key - digit
        b. value - number of occurrences
    4. Iterating over numbers check if number is already in `result`:
        a. If first occurrence, then add it to `result` with value 1
        b. If exists, then increment the value by 1
    5. Run doctests - all must succeed

Polish:
    1. Iteruj po `DATA`
    2. Policz wystąpienia każdej z cyfr
    3. Stwórz pusty `result: dict[int, int]`:
        a. klucz - cyfra
        b. wartość - liczba wystąpień
    4. Iterując po cyfrach sprawdź czy cyfra znajduje się już w `result`:
        a. Jeżeli pierwsze wystąpienie, to dodaj ją do `result` z wartością 1
        b. Jeżeli istnieje, to zwiększ w wartość o 1
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict
    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())
    >>> assert all(x in result.keys() for x in range(0, 10))

    >>> result
    {1: 7, 4: 8, 6: 4, 7: 4, 5: 4, 0: 7, 9: 5, 8: 6, 2: 2, 3: 3}
"""

DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
        0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
        1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

# dict[int,int]: number of occurrences of each digit from DATA
result = ...

