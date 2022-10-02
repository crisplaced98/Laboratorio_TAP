from abc import abstractmethod, ABC
class AComponent(ABC):
    @abstractmethod
    def ls(self):
        pass
    @abstractmethod
    def collect(self):
        pass
    @abstractmethod
    def toList(self):
        pass
    @abstractmethod
    def search(self, name):
        pass
    @abstractmethod
    def setParent(self, parent):
        pass
    @abstractmethod
    def size(self):
        pass