from abc import ABC, abstractmethod
class ComputerPartVisitor(ABC):
    @abstractmethod
    def visitComputer(self, computer):
        pass

    @abstractmethod
    def visitMouse(self, mouse):
        pass

    @abstractmethod
    def visitKeyboard(self, keyboard):
        pass

    @abstractmethod
    def visitMonitor(self, monitor):
        pass