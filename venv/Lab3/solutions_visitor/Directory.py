from Lab3.solutions_visitor.AComponent import AComponent
from collections import deque
#Composite -> Representa los componentes complejos que puede que tengan hijos
class Directory(AComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = []
        self.__parent = None

    def addChild(self, child):
        self.__children.append(child)
        child.setParent(self)

    def removeChild(self, child):
        self.__children.remove(child)

    def ls(self):
        print(self.__name)
        for child in self.__children:
            child.ls()

    def setParent(self, parent):
        self.__parent = parent

    def __str__(self):
        path = "/"
        if self.__parent != None:
            path = str(self.__parent) + "/"
        return path + str(self.__name)

    def toList(self):
        result = []
        result.append(self)
        for child in self.__children:
            result.extend(child.toList())
        return result

    @property
    def children(self):
        return self.__children

    def accept(self, v):
        v.visitDirectory(self)