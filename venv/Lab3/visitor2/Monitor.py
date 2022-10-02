from Lab3.visitor2.ComputerPart import ComputerPart
class Monitor(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visitMonitor(self)