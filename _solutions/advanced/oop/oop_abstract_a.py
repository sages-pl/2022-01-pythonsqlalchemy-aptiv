
from abc import ABC, abstractmethod


class IrisAbstract(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(IrisAbstract):
    def get_name(self):
        pass
