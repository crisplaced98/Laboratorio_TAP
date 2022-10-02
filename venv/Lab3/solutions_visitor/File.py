from Lab3.solutions_visitor.AComponent import AComponent
from collections import deque

# Leaf -> Representa el ibjeto final de una composición
class File(AComponent):
    def __init__(self, name, size, owner):
        super(File, self).__init__()
        self.__name = name
        self.__size = size
        self.__owner = owner
        self.__parent = ""

    def ls(self):
        print(self.__name)

    def setParent(self, parent):
        self.__parent = parent

    def __str__(self):
        path = str(self.__parent) + "/"
        return path + str(self.__name)

    def toList(self):
        result = []
        result.append(self)
        return result

    @property
    def owner(self):
        return self.__owner

    def getsize(self):
        return self.__size
    
    def setsize(self, size):
        self.__size = size

    def accept(self, v):
        v.visitFile(self)
