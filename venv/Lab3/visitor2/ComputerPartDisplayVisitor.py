from Lab3.visitor2.ComputerPartVisitor import ComputerPartVisitor
class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visitComputer(self, computer):
        print("Displaying Computer")
    def visitMouse(self, mouse):
        print("Displaying Mouse")
    def visitKeyboard(self, keyboard):
        print("Displaying keyboard")
    def visitMonitor(self, monitor):
        print("Displaying monitor")