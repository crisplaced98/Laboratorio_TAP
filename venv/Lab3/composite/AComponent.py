from abc import abstractmethod, ABC
class AComponent(ABC):
    @abstractmethod
    def size(self):
        pass