# Element
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def accept(self, v):
        pass
