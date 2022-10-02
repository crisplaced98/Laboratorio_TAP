from Lab1.interfaces.Bop import Bop
from Lab1.interfaces.Musician import Musician
from Lab1.interfaces.Thing import Thing
class UseThing:
    def sings(m):
        m.sing()
    def dances(b):
        b.dance()

    c = Thing()
    sings(c)
    dances(c)

    music = c
    dance = c

    music.sing()
    dance.dance()

    music = dance
    music.sing()