"""
* Assignment: Decorator Method Alive
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Create `if_alive` method decorator
    2. Decorator will allow running `make_damage` method
       only if `current_health` is greater than 0
    3. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator metody `if_alive`
    2. Dekorator pozwoli na wykonanie metody `make_damage`,
       tylko gdy `current_health` jest większe niż 0
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> class Hero:
    ...    def __init__(self, name):
    ...        self.name = name
    ...        self.current_health = 100
    ...
    ...    @if_alive
    ...    def make_damage(self):
    ...        return 10

    >>> hero = Hero('Jan Twardowski')
    >>> hero.make_damage()
    10
    >>> hero.current_health = -10
    >>> hero.make_damage()
    Traceback (most recent call last):
    RuntimeError: Hero is dead and cannot make damage
"""

def if_alive(method):
    def wrapper(hero, *args, **kwargs):
        return method(hero, *args, **kwargs)
    return wrapper


