from abc import abstractmethod, ABC
class Observer(ABC):
    @abstractmethod
    def notifyAdd(self, elem):
        pass
    @abstractmethod
    def notifyRemove(self, elem):
        pass