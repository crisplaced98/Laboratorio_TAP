from abc import ABC, abstractmethod
class ICorrupt(ABC):
    def spendLikeCrazy(self):
        print("Restaurants, parties, vacations, ...")
    @staticmethod
    def blackCard():
        print("spending money ...")