from Lab2.stacks.ArrayStack import ArrayStack
from Lab2.stacks.VectorStack import VectorStack
class UsaStack:

    def test(p):
        i = 0
        while not p.llena():
            p.push(10*i)
            i +=1

        while not p.vacia():
            print(p.pop())

    def test2(self, p):
        while not p.vacia():
            print(p.pop())

    lista = [None]*5
    pila = ArrayStack(lista)
    pila.push(3000)
    pila.push(7000)
    pila.push(9000)

    for i in pila:
        print(i)

    test(pila)

    pila = VectorStack(10)
    pila.push(3)
    pila.push(7)
    pila.push(9)

    for i in pila:
        print(i)
    test(pila)