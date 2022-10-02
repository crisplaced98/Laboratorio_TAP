from copy import copy
class Car:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price

    def __eq__(self, other):
        return (other.__price == self.__price and other.__brand == self.__brand)

    def __str__(self):
        return ("(" + str(self.__brand) + "," +str(self.__price) +")")
    
    def __copy__(self):
        return (Car(self.__brand, self.__price))

    #Definimos getters y setters porque son variables privadas
    @property
    def brand(self):
        return self.__brand
    
    @property
    def price(self):
        return self.__price
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
    
    @price.setter
    def price(self, price):
        self.__price = price



