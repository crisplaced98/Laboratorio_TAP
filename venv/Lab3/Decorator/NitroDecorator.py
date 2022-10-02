from Lab3.Decorator.Car import Car
#Decorador concreto
class NitroDecorator(Car):
    def __init__(self, car):
        super().__init__("",0)
        self.__client = car

    @property
    def description(self):
        return self.__client.description + ' with nitrous oxide system'

    @property
    def price(self):
        return self.__client.price + 7000