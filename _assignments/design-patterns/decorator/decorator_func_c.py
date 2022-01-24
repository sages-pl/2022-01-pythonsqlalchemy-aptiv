"""
* Assignment: Decorator Function Check
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Create decorator `check`
    2. Decorator calls function, only when `echo.disabled` is `False`
    3. Note that decorators overwrite references and in `wrapper`
       you must check if `wrapper.disabled` is `False`
    4. Else raise an exception `PermissionError`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator `check`
    2. Dekorator wywołuje funkcję, tylko gdy `echo.disabled` jest `False`
    3. Zwróć uwagę, że dekoratory nadpisują referencje i we `wrapper`
       musisz sprawdzić czy `wrapper.disabled` jest `False`
    4. W przeciwnym przypadku podnieś wyjątek `PermissionError`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @check
    ... def echo(text):
    ...     print(text)

    >>> from inspect import isfunction
    >>> assert isfunction(check)
    >>> assert isfunction(check(lambda: None))
    >>> assert isfunction(echo)

    >>> echo.disabled = False
    >>> echo('hello')
    hello

    >>> echo.disabled = True
    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled

    >>> assert hasattr(echo, 'disabled')
"""

def check(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


