from abc import ABC, abstractmethod
class Talkative(ABC):
    @abstractmethod
    def talk(self):
        pass