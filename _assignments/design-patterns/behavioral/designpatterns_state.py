"""
* Assignment: DesignPatterns Behavioral State
* Complexity: medium
* Lines of code: 34 lines
* Time: 21 min

English:
    1. Implement State pattern
    2. Then add another language:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec State
    2. Następnie dodaj nowy język:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> polish = Translation(Polish())
    >>> english = Translation(English())
    >>> chinese = Translation(Chinese())

    >>> polish.hello()
    'Cześć'
    >>> polish.goodbye()
    'Do widzenia'

    >>> english.hello()
    'Hello'
    >>> english.goodbye()
    'Goodbye'

    >>> chinese.hello()
    '你好'
    >>> chinese.goodbye()
    '再见'
"""
from enum import Enum


class Language(Enum):
    POLISH = 'pl'
    ENGLISH = 'en'
    RUSSIAN = 'ru'


class Translation:
    __language: Language

    def __init__(self, language: Language):
        self.__language = language

    def hello(self) -> str:
        if self.__language is Language.POLISH:
            return 'Cześć'
        elif self.__language is Language.ENGLISH:
            return 'Hello'
        elif self.__language is Language.RUSSIAN:
            return 'Здравствуй'
        else:
            return 'Unknown language'

    def goodbye(self) -> str:
        if self.__language is Language.POLISH:
            return 'Do widzenia'
        elif self.__language is Language.ENGLISH:
            return 'Goodbye'
        elif self.__language is Language.RUSSIAN:
            return 'До свидания'
        else:
            return 'Unknown language'


