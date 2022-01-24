"""
* Assignment: FuncProg Closure Call
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define function `check` with parameter `func: Callable`
    2. Define closure function `wrapper` inside `check`
    3. Function `wrapper` takes:
       - arbitrary number of positional arguments
       - arbitrary number of keyword arguments
    4. Function `wrapper` prints `hello from wrapper` on the screen
    5. Function `check` must return `wrapper: Callable`
    6. Define function `hello()` which prints `hello from function`
    7. Define `result` with result of calling `check(hello)`
    8. Delete `check` using `del` keyword
    9. Call `result`
    10. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `check` z parametrem `func: Callable`
    2. Zdefiniuj funkcję closure `wrapper` wewnątrz `check`
    3. Funkcja `wrapper` przyjmuje:
       - dowolną ilość argumentów pozycyjnych
       - dowolną ilość argumentów nazwanych
    4. Funkcja `wrapper` wypisuje `hello from wrapper`
    5. Funkcja `check` ma zwracać `wrapper: Callable`
    6. Zdefiniuj funkcję `hello()`, która wypisuje `hello from function`
    7. Zdefiniuj zmienną `result`, która jest wynikiem wywołania `check(hello)`
    8. Skasuj `check` za pomocą słowa kluczowego `del`
    9. Wywołaj `result`
    10. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(hello)
    >>> assert isfunction(result)
    >>> assert not hasattr(__name__, 'check')

    >>> hello()
    hello from function

    >>> result()
    hello from wrapper

    >>> check()
    Traceback (most recent call last):
    NameError: name 'check' is not defined
"""

# Callable: parameter: func; inside: wrapper with args, kwargs; return: wrapper
def check():
    ...

# Callable: prints `hello from function`
def hello():
    ...

# callable: call check(hello); delete check; call result
result = ...


