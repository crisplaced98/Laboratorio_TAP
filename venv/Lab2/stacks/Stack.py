from abc import ABC, abstractmethod

class Stack(ABC):
    @abstractmethod
    def push(self, elem):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def llena(self):
        pass

    @abstractmethod
    def vacia(self):
        pass
