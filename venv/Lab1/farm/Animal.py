class Animal:
    def __init__(self, patas, ojos):
        self._patas = patas
        self.__ojos = ojos

    @property
    def patas (self):
         return self._patas
    @patas.setter
    def patas (self, patas):
        self._patas = patas

    @property
    def ojos (self):
        return self.__ojos
    @ojos.setter
    def ojos (self, ojos):
        self.__ojos = ojos

    def habla(self):
        return 'I am an animal'