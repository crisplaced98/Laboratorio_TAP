from Lab3.composite.AComponent import AComponent
from collections import deque
#Composite -> Representa los componentes complejos que puede que tengan hijos
class Directory(AComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = deque()

    def addChild(self, child):
        self.__children.append(child)

    def removeChild(self, child):
        self.__children.remove(child)

    def size(self):
        result = 0
        for child in self.__children:
            result = result + child.size()
        return result