from Lab1.interfaces.Bop import Bop
from Lab1.interfaces.Musician import Musician
class Thing(Bop, Musician):
    def sing(self):
        print("ouch...")
    def dance(self):
        print("LALALA")