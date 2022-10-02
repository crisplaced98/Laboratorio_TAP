from collections.abc import Iterator, Iterable
from abc import abstractmethod, ABC
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass