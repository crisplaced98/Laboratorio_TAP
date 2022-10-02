from Lab1.farm.Animal import Animal
from Lab1.farm.Cat import Cat
from Lab1.farm.Dog import Dog
from Lab1.farm.Parrot import Parrot
from Lab1.farm.MutantParrot import MutantParrot
import collections
class UsaAnimal2:
    a = Animal (3,3)
    g = Cat(1, 2)
    lM = MutantParrot(3, 3)

    #Si granja estuviera definida para guardar objetos de tipo Animal, podríamos guardar gatos y lorosMutantes, pero solo podrían
    #utilizar los métodos que estén en Animal, no los extra
    granja = [a, g, lM]
    for ani in granja:
        print(ani.habla())

    #Python no tiene una librería de LinkedList construída. Para esto vamos a utilizar el package deque().
    camion = collections.deque()
    camion.append(a)
    camion.append(g)
    camion.append(lM)

    for o in camion:
        #No hay casting en Python
        #x = Animal(o)
        print(f'{o.habla()}')
