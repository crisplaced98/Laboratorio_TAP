from Lab3.visitor2.Computer import Computer
from Lab3.visitor2.ComputerPartDisplayVisitor import ComputerPartDisplayVisitor
class Test:
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())