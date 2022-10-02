from Lab3.composite.AComponent import AComponent
#Leaf -> Representa el ibjeto final de una composición
class File(AComponent):
    def __init__(self, name, size):
        super(File, self).__init__()
        self.__name = name
        self.__size = size

    def size(self):
        return self.__size
    
    

