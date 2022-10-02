from abc import ABC, abstractmethod
class IMap(ABC):
    @abstractmethod
    def apply(self, elem):
        pass