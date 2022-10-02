from Lab1.farm.Animal import Animal
class Parrot (Animal):
    def __init__(self, patas, ojos):
        super().__init__(patas, ojos)
    def habla(self):
        return 'Soy un Loro y ' +super().habla()