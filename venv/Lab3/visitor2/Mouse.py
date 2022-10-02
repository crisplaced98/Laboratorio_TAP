from Lab3.visitor2.ComputerPart import ComputerPart
class Mouse(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visitMouse(self)