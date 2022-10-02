from abc import abstractmethod, ABC
#Declara las operaciones comunes para el proxy y el subject real
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

    