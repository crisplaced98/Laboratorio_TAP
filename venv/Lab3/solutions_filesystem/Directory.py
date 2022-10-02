from Lab3.solutions_filesystem.AComponent import AComponent
from collections import deque
#Composite -> Representa los componentes complejos que puede que tengan hijos
class Directory(AComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = []
        self.__parent = ""

    def addChild(self, child):
        self.__children.append(child)
        child.setParent(self)

    def removeChild(self, child):
        self.__children.remove(child)

    def ls(self):
        print(self.__name)
        for child in self.__children:
            child.ls()

    def search(self, name):
        result = []
        for child in self.__children:
            result.append(child.search("lp"))
        return result
    def setParent(self, parent):
        self.__parent = parent

    def collect(self):
        result = []
        print("hola")
        for child in self.__children:
            print(result)
            result.append(child)
        return result
    def __str__(self):
        path = "/"
        if (self.__parent != None):
            path = str(self.__parent) + "/"
        return path + str(self.__name)

    def toList(self):
        result = []
        result.append(self)
        for child in self.__children:
            result.append(child.toList())
        return result
    
    def size(self):
        result = 0
        for child in self.__children:
            result = result + child.size()
        return result