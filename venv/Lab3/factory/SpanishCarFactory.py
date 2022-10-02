from Lab3.factory.AbstractCarFactory import AbstractCarFactory
from Lab3.factory.SpanishCar import SpanishCar


class SpanishCarFactory(AbstractCarFactory):
    def createCar(self):
        return SpanishCar()