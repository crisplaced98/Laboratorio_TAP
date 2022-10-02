from Lab2.generics.Thing2 import Thing2
from Lab2.generics.Cat import Cat


class UseThing2:
    g = Cat(1, 2)
    c = Thing2(g)
    c.nombre = g

    g2 = c.nombre
    a = c.nombre
    print(g2.habla())
    print(a.habla())

    #En Java esto es ilegal. En Python no.
    c = Thing2('www')
    print(c.nombre)

