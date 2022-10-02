from abc import abstractmethod, ABC
class ComputerPart(ABC):
    @abstractmethod
    def accept(self, computerPartVisitor):
        pass