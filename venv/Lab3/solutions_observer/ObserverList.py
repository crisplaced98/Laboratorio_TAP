from abc import abstractmethod, ABC
class ObserverList(ABC):
    @abstractmethod
    def register(self, observer):
        pass
    @abstractmethod
    def unregister(self, observer):
        pass
    @abstractmethod
    def add(self, elem):
        pass
    @abstractmethod
    def remove(self, elem):
        pass
    