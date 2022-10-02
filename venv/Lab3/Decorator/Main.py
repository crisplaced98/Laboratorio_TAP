from Lab3.Decorator.Car import Car
from Lab3.Decorator.NitroDecorator import NitroDecorator
from Lab3.Decorator.SpoilerDecorator import SpoilerDecorator

class Main:
    myCar = Car('Chevrolet', 10000)
    decorator = SpoilerDecorator(myCar)
    decorator2 = NitroDecorator(decorator)

    #Let's decorate
    myCar = NitroDecorator(myCar)
    myCar = SpoilerDecorator(myCar)

    car = SpoilerDecorator(NitroDecorator(Car('Chevrolet', 10000)))

    print(f'Description myCar: {myCar.description}')
    print(f'Price myCar: {myCar.price} €')

    print(f'Description decorator2: {decorator2.description}')
    print(f'Price decorator2: {decorator2.price} €')

    print(f'Description car: {car.description}')
    print(f'Price car: {car.price} €')