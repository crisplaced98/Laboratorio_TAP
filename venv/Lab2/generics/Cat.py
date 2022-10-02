from Lab2.generics.Animal import Animal
class Cat (Animal):
    def __init__(self, patas, ojos):
        super().__init__(patas, ojos)
    def habla(self):
        return "I'm a cat"