
from abc import ABC, abstractmethod


class Language(ABC):
    @abstractmethod
    def hello(self) -> str: ...

    @abstractmethod
    def goodbye(self) -> str: ...


class Polish(Language):
    def goodbye(self) -> str:
        return 'Do widzenia'

    def hello(self) -> str:
        return 'Cześć'


class English(Language):
    def goodbye(self) -> str:
        return 'Goodbye'

    def hello(self) -> str:
        return 'Hello'


class Russian(Language):
    def goodbye(self) -> str:
        return 'До свидания'

    def hello(self) -> str:
        return 'Здравствуй'


class Chinese(Language):
    def goodbye(self) -> str:
        return '再见'

    def hello(self) -> str:
        return '你好'


class Translation:
    __language: Language

    def __init__(self, language: Language):
        self.__language = language

    def goodbye(self):
        return self.__language.goodbye()

    def hello(self):
        return self.__language.hello()
