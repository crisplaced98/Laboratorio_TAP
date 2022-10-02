from Lab3.solutions_visitor.Visitor import Visitor
class OwnerVisitor(Visitor):
    def __init__(self, owner):
        self.__results = []
        self.__owner = owner
    def visitFile(self, file):
        if (file.owner == self.__owner):
            self.__results.append(file)

    @property
    def results(self):
        return self.__results