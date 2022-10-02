from abc import ABC, abstractmethod
class Imap(ABC):
    @abstractmethod
    def apply(self, elem):
        pass