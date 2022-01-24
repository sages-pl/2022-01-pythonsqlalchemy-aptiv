""""
* Assignment: Decorator Function Abspath
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Absolute path is when `path` starts with `current_directory`
    2. Create function decorator `abspath`
    3. If `path` is relative, then `abspath` will convert it to absolute
    4. If `path` is absolute, then `abspath` will not modify it
    5. Run doctests - all must succeed

Polish:
    1. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
    2. Stwórz funkcję dekorator `abspath`
    3. Jeżeli `path` jest względne, to `abspath` zamieni ją na bezwzględną
    4. Jeżeli `path` jest bezwzględna, to `abspath` nie będzie jej modyfikował
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Path(filename).absolute()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @abspath
    ... def display(path):
    ...     return str(path)

    >>> current_dir = str(Path().cwd())
    >>> display('iris.csv').startswith(current_dir)
    True
    >>> display('iris.csv').endswith('iris.csv')
    True
    >>> display('/home/python/iris.csv')
    '/home/python/iris.csv'
"""

from pathlib import Path


