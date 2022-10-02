#Componente
class Car:
    def __init__(self, description, price):
        self.__description = description
        self.__price = price

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price