from abc import abstractmethod, ABC
class AComponent(ABC):
    @abstractmethod
    def ls(self):
        pass

    @abstractmethod
    def toList(self):
        pass

    @abstractmethod
    def setParent(self, parent):
        pass

    @abstractmethod
    def accept(self, v):
        pass