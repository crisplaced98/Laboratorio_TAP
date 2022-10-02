from abc import ABC, abstractmethod

#Contrato
class AbstractCarFactory(ABC):
    @abstractmethod
    def createCar(self):
        pass