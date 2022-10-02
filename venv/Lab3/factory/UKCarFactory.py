from Lab3.factory.AbstractCarFactory  import AbstractCarFactory
from Lab3.factory.UKCar  import UKCar


class UKCarFactory(AbstractCarFactory):
    def createCar(self):
        return UKCar()