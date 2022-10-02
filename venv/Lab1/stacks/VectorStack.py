from Lab1.stacks.Stack import Stack
class VectorStack(Stack):
    def __init__(self, max):
        self.__monton = []
        self.__max = max
        self.__cnt = 0
    def push(self, elem):
        self.__monton.append(elem)
        self.__cnt = self.__cnt + 1
    def pop(self):
        elem = self.__monton.pop()
        self.__cnt = self.__cnt - 1
        return elem
    def llena(self):
        return (self.__max == self.__cnt)
    def vacia(self):
        return (self.__cnt == 0)