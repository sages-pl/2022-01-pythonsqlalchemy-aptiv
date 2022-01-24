"""
* Assignment: OOP Classmethod Time
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Define class `Timezone` with:
       a. Field `when: datetime`
       b. Field `tzname: str`
       c. Method `convert()` taking class and `datetime` as arguments
    2. Method `convert()` returns instance of a class, which was given
       as an argument with field set `when: datetime`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Timezone` z:
       a. polem `when: datetime`
       b. polem `tzname: str`
       c. Metodą `convert()` przyjmującą klasę oraz `datetime` jako argumenty
    2. Metoda `convert()` zwraca instancję klasy, którą dostała jako argument
       z ustawionym polem `when: datetime`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Timezone)
    >>> assert isclass(CET)
    >>> assert isclass(CEST)

    >>> dt = datetime(1969, 7, 21, 2, 56, 15)

    >>> cet = CET.convert(dt)
    >>> assert cet.tzname == 'Central European Time'
    >>> assert cet.when == datetime(1969, 7, 21, 2, 56, 15)

    >>> cest = CEST.convert(dt)
    >>> assert cest.tzname == 'Central European Summer Time'
    >>> assert cest.when == datetime(1969, 7, 21, 2, 56, 15)
"""
from datetime import datetime


class Timezone:
    tzname: str


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'


