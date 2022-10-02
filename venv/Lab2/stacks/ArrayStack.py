from Lab2.stacks.Stack import Stack

class ArrayStack(Stack):
    cnt = 0

    def __init__(self, lista):
        self.__monton = lista
        self.__cima = 0

    def push(self, elem):
        self.__monton[self.__cima] = elem
        self.__cima = self.__cima + 1

    def pop(self):
        self.__cima = self.__cima - 1
        return self.__monton[self.__cima]

    def llena(self):
        return self.__cima == len(self.__monton)

    def vacia(self):
        return self.__cima == 0

    def __iter__(self):
        return self

    def __next__(self):
        print('Avanza')
        self.cnt = self.cnt + 1
        if self.cnt > self.__cima:
            raise StopIteration
        return self.__monton[self.cnt - 1]


    def hasNext(self):
        return self.cnt < self.__cima
