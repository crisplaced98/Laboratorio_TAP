from Lab3.solutions_filesystem2.AComponent import AComponent
from Lab3.solutions_filesystem2.ExistException import ExistException

# Composite -> Representa los componentes complejos que puede que tengan hijos
class Directory(AComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = []
        self.__parent = ""

    def addChild(self, child):
        if(self.__children.__contains__(child)):
            raise ExistException("Ya existe")
        self.__children.append(child)
        child.setParent(self)

    def removeChild(self, child):
        self.__children.remove(child)

    def ls(self):
        print(self.__name)
        for child in self.__children:
            child.ls()

    def collect(self):
        result = []
        result.append(self.__name)
        for child in self.__children:
            result.append(child.collect())
        return result

    def search(self, name):
        result = []
        aux = []
        for child in self.__children:
            aux = child.search("lp")
            if (len(aux)>0):
                result.append(child.search("lp"))
                print(str(result[0])) 
        return result

    def setParent(self, parent):
        self.__parent = parent

    def getName(self):
        return self.__name
 

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