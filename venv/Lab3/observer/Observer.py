from abc import abstractmethod, ABC
#La interfaz del observador declara el método update, que es utilizada por los subjects
class Observer(ABC):
    @abstractmethod
    def update(self, newValue):
        pass
    