from abc import abstractmethod, ABC
class Container(ABC):
    @abstractmethod
    def iterator(self):
        pass