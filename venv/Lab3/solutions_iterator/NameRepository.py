class NameRepository:
    names = ["Robert", "John", "Julie", "Lora"]

    def __iter__(self):
        self.__index = 0
        return self

    '''En Python no se necesita el hasNext para implementar ya que no existe. El final de la iteración se indica con
    una excepción: StopIteration'''
    def __next__(self):
        if self.__index >= len(self.names):
            raise StopIteration
        elem = self.names[self.__index]
        self.__index += 1
        return elem

