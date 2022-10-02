from abc import ABC, abstractmethod
#Esta interfaz es común a todas las estrategias concretas. Declara un método que la clase Context utiliza para ejecutar la estrategia
class Strategy(ABC):
    @abstractmethod
    def doOperation(self, num1, num2):
        pass