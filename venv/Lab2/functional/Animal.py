class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return ("Animal{ name = '"+ str(self.__name)+"', age = " +str(self.__age)+ "}")

    @property
    def name (self):
         return self.__name
    @name.setter
    def patas (self, name):
        self.__name = name

    @property
    def age (self):
        return self.__age
    @age.setter
    def ojos (self, age):
        self.__age = age

    def talk(self):
        return 'Hola'