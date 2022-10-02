from Lab3.solutions_filesystem.AComponent import AComponent
from collections import deque

# Leaf -> Representa el objeto final de una composición
class File(AComponent):
    def __init__(self, name, size=0):
        super(File, self).__init__()
        self.__name = name
        self.__size = size
        self.__parent = ""

    def ls(self):
        print(self.__name)

    def collect(self):
        result = []
        result.extend(self.__name)

    def search(self, name):
        result = []
        if (self.__name == name):
            result.append(self)
        return result

    def setParent(self, parent):
        self.__parent = parent

    def __str__(self):
        path = str(self.__parent) + "/"
        return path + str(self.__name)

    def toList(self):
        result = []
        result.append(self)
        return result

    def size(self):
        return self.__size
