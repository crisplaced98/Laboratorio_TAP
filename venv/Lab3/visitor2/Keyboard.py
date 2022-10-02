from Lab3.visitor2.ComputerPart import ComputerPart
class Keyboard(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visitKeyboard(self)