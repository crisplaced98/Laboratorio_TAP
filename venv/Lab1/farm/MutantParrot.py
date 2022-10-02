from Lab1.farm.Parrot import Parrot
class MutantParrot (Parrot):
    def __init__(self, patas, ojos):
        super().__init__(patas, ojos)
    def vuela(self):
        return 'vuelo...'