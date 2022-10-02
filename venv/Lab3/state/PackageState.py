from abc import abstractmethod, ABC
class PackageState(ABC):
    @abstractmethod
    def next(self, pkg):
        pass
    @abstractmethod
    def prev(self, pkg):
        pass
    @abstractmethod
    def printStatus(self):
        pass