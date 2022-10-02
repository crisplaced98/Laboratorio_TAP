from abc import abstractmethod, ABC
class Visitor:
    @abstractmethod
    def visitFile(self, file):
        pass
    def visitDirectory(self, directory):
        for elem in directory.children:
            elem.accept(self)
