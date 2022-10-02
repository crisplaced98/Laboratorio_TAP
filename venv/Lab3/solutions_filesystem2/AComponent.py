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
    @abstractmethod
    def getName(self):
        pass
    
    def __eq__(self, other):
        return (self.getName() == other.getName())