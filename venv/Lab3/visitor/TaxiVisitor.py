from abc import ABC, abstractmethod


class TaxiVisitor(ABC):
    @abstractmethod
    def visitHasty(self, e):
        pass

    @abstractmethod
    def visitLeisurely(self, e):
        pass