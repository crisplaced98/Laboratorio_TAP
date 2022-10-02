from Lab1.farm.Animal import Animal
class Dog (Animal):
    def __init__(self, patas, ojos, pulgas):
        super().__init__(patas, ojos)
        self._pulgas = pulgas

    @property
    def pulgas(self):
        return self._pulgas
    @pulgas.setter
    def pulgas(self, pulgas):
        self._pulgas = pulgas

    def cambiaPadre(self):
        self.patas = 3
        self.ojos = 5

    def habla(self):
        return ('Pulgas ' +str(self._pulgas))