class Person:
    def __init__(self, dni, name, age):
        self.__dni = dni
        self.__name = name
        self.__age = age

    def __str__(self):
        return ("Person{dni = '" +str(self.__dni) + "', name = '" +str(self.__name)+"'}")

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni = dni