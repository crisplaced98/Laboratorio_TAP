from abc import abstractmethod, ABC

class Musician(ABC):
    @abstractmethod
    def sing(self):
        pass
