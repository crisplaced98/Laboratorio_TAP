from Lab3.solutions_visitor.Visitor import Visitor
class SearchVisitor(Visitor):
    def __init__(self, name):
        self.__results = []
        self.__name = name
    def visitFile(self, file):
        if (file.name == self.__name):
            self.__results.append(file)

    @property
    def results(self):
        return self.__results