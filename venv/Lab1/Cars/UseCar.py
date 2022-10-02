from Lab1.Cars.Car import Car
from Lib import copy
class UseCar:
    #Create cars
    myCar = Car("bmw", 100)
    otherCar = Car("seat", 10)
    copy = Car("seat", 10)

    #Compare memory addresses
    '''Para comparar direcciones de memoria en Python se tiene que utilizar el id'''
    if(id(otherCar) == id(copy)):
        print("equals == otherCar and copy")

    #Use method equals
    if(otherCar == copy):
        print("equals otherCar and copy")

    if(myCar == otherCar):
        print("equals myCar and otherCar")

    print("My car: " + str(myCar))
    peugeot = Car("peugeot", 900)
    renault = peugeot

    peugeot.brand = "mercedes"
    print("Renault: " +str(renault))
    print("Peugeot: " +str(peugeot))

    audi = Car("audi", 900)
    renault = audi.__copy__()
    renault.brand = "ferrari"
    print("Renault: " +str(renault))
    print("Audi: " +str(audi))


