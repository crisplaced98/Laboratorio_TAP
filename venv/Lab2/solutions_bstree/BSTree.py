class BSTree:
    def __init__(self, comp, data=None):
        self.__comp = comp
        self.__left = None
        self.__right = None
        self.__data = data

    def insert(self, elem):
        if (self.__data == None):
            self.__data = elem
        else:
            if (self.__comp.compare(elem, self.__data) <=0):
                if(self.__left == None):
                    self.__left = BSTree(self.__comp, elem)
                else:
                    self.__left.insert(elem)
            else:
                if (self.__right == None):
                    self.__right = BSTree(self.__comp, elem)
                else:
                    self.__right.insert(elem)

    def contains(self, elem):
        if (self.__data == elem):
            return True
        else:
            if(self.__comp.compare(elem, self.__data) <=0):
                if (self.__left != None):
                    return self.__left.contains(elem)
                else:
                    return False
            else:
                if(self.__right != None):
                    return self.__right.contains(elem)
                else:
                    return False

    def tree2List(arbol):
        list = []
        if (arbol.__data != None):
            list.append(arbol.__data)
            if (arbol.__left != None):
                list.append(BSTree.tree2List(arbol.__left))
            if(arbol.__right != None):
                list.append(BSTree.tree2List(arbol.__right))
        return list
                
    def __iter__(self):
        lista = BSTree.tree2List(self)
        return lista.__iter__()