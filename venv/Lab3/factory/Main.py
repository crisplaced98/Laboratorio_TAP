from Lab3.factory.SpanishCarFactory import SpanishCarFactory
from Lab3.factory.UKCarFactory import UKCarFactory

class Main:
    factory = SpanishCarFactory()

    '''the client can work with the factory in an unique way, regardless of
    its specific type. He also can create a car and use it without knowing
    details of its creation and its specific type'''
    #Asignación polimorfica
    car = factory.createCar()
    print("Spanish car: " +car.getDriverSide())
    
    factory2 = UKCarFactory()
    car2 = factory2.createCar()
    print("English car: " +car2.getDriverSide())