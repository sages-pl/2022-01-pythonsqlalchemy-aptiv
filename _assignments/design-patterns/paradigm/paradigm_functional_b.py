"""
* Assignment: Balanced Brackets
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Create function which checks if brackets are balanced
    2. Brackets are balanced, when each opening bracket has closing pair
    3. Use recursion
    4. Types of brackets:
        a. round: `(` i `)`
        b. square: `[` i `]`
        c. curly `{` i `}`
        d. angle `<` i `>`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję, która sprawdzi czy nawiasy są zbalansowane
    2. Nawiasy są zbalansowane, gdy każdy otwierany nawias ma zamykającą parę
    3. Użyj rekurencji
    4. Typy nawiasów:
        a. okrągłe: `(` i `)`
        b. kwadratowe: `[` i `]`
        c. klamrowe `{` i `}`
        d. trójkątne `<` i `>`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_bracket_balanced('{}')
    True
    >>> is_bracket_balanced('()')
    True
    >>> is_bracket_balanced('[]')
    True
    >>> is_bracket_balanced('<>')
    True
    >>> is_bracket_balanced('')
    True
    >>> is_bracket_balanced('(')
    False
    >>> is_bracket_balanced('}')
    False
    >>> is_bracket_balanced('(]')
    False
    >>> is_bracket_balanced('([)')
    False
    >>> is_bracket_balanced('[()')
    False
    >>> is_bracket_balanced('{()[]}')
    True
    >>> is_bracket_balanced('() [] () ([]()[])')
    True
    >>> is_bracket_balanced("( (] ([)]")
    False
"""

BRACKET_OPEN = ('(', '{', '[', '<')
BRACKET_CLOSE = (')', '}', ']', '>')
PAIRS = dict(zip(BRACKET_OPEN, BRACKET_CLOSE))


