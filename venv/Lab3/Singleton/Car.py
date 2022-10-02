from Lab3.Singleton.SingletonMeta import SingletonMeta
class Car(metaclass=SingletonMeta):
    __fuelLevel = 0
    __car = None
    def fillUp(self):
        self.__fuelLevel = 4
    @property
    def car(self):
        return self.__car
    
    def run(self):
        if (self.__fuelLevel == 0):
            print("Fill up please")
        else:
            self.__fuelLevel -= 1
            print("Ruuuuuuun!!")