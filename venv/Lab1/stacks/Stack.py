'''En Python no son necesarias las interfaces ya que Python tiene herencia múltiple y ducktyping
    (tipificación dinámica de datos) https://ellibrodepython.com/abstract-base-class
    Para que se obligue a que se implementen estos métodos usaremos el "abstractmethod'''
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
