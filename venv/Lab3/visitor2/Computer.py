from Lab3.visitor2.Mouse import Mouse
from Lab3.visitor2.Keyboard import Keyboard
from Lab3.visitor2.Monitor import Monitor
from Lab3.visitor2.ComputerPart import ComputerPart

class Computer(ComputerPart):
    def __init__(self):
        self.__parts = [Mouse(), Keyboard(), Monitor()]

    def accept(self, computerPartVisitor):
        for i in self.__parts:
            i.accept(computerPartVisitor)
        computerPartVisitor.visitComputer(self)