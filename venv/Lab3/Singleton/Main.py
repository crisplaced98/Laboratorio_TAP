from Lab3.Singleton.Car import Car
class Main:
    myCar = Car()
    myCar.run()
    myCar.fillUp()
    myCar.run()

    myCar2 = Car()
    myCar2.run()