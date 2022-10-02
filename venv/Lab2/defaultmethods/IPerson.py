from abc import ABC, abstractmethod
class IPerson(ABC):
    @abstractmethod
    def sayHello(self):
        pass
    @staticmethod
    def blackCard():
        print("I have a black card")