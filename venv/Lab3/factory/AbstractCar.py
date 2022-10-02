from abc import ABC, abstractmethod
#Creator -> Declara el metodo de la factoria que se supone que tiene que devolver un objeto
#Contrato
#An interface is chosen instead an abstract class
#because in this example aren't needed attributes and methods already implemented
class AbstractCar(ABC):
    @abstractmethod
    def getDriverSide(self):
        pass