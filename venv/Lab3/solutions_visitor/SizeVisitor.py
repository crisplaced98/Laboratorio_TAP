from Lab3.solutions_visitor.Visitor import Visitor
from Lab3.solutions_visitor.File import File
class SizeVisitor(Visitor):
    __size = 0

    def getsize(self):
        return self.__size

    def visitFile(self, file):
        self.__size+= file.getsize()

