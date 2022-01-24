"""
* Assignment: Sequence Set Create
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create sets:
        a. `result_a` with elements: 1, 2, 3
        b. `result_b` with elements: 1.1, 2.2, 3.3
        c. `result_c` with elements: 'a', 'b', 'c'
        d. `result_d` with elements: True, False
        e. `result_e` with elements: 1, 2.2, True, 'a'
    2. Run doctests - all must succeed

Polish:
    1. Stwórz sety:
        a. `result_a` z elementami: 1, 2, 3
        b. `result_b` z elementami: 1.1, 2.2, 3.3
        c. `result_c` z elementami: 'a', 'b', 'c'
        d. `result_d` z elementami: True, False, True
        e. `result_e` z elementami: 1, 2.2, True, 'a'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign result to variable: `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign result to variable: `result_d`'
    >>> assert result_e is not Ellipsis, \
    'Assign result to variable: `result_e`'

    >>> assert type(result_a) is set, \
    'Variable `result_a` has invalid type, should be set'
    >>> assert type(result_b) is set, \
    'Variable `result_b` has invalid type, should be set'
    >>> assert type(result_c) is set, \
    'Variable `result_c` has invalid type, should be set'
    >>> assert type(result_d) is set, \
    'Variable `result_d` has invalid type, should be set'
    >>> assert type(result_e) is set, \
    'Variable `result_e` has invalid type, should be set'

    >>> assert result_a == {1, 2, 3}, \
    'Variable `result_a` has invalid value, should be {1, 2, 3}'
    >>> assert result_b == {1.1, 2.2, 3.3}, \
    'Variable `result_b` has invalid value, should be {1.1, 2.2, 3.3}'
    >>> assert result_c == {'a', 'b', 'c'}, \
    'Variable `result_c` has invalid value, should be {"a", "b", "c"}'
    >>> assert result_d == {True, False}, \
    'Variable `result_d` has invalid value, should be {True, False}'
    >>> assert result_e == {1, 2.2, True, 'a'}, \
    'Variable `result_e` has invalid value, should be {1, 2.2, True, "a"}'
"""

# set[int]: with elements: 1, 2, 3
result_a = ...

# set[float]: with elements: 1.1, 2.2, 3.3
result_b = ...

# set[str]: with elements: 'a', 'b', 'c'
result_c = ...

# set[bool]: with elements: True, False
result_d = ...

# set[int|float|bool|str]: with elements: 1, 2.2, True, 'a'
result_e = ...

