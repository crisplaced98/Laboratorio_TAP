class Customer:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__address = ""
        self.__phoneNumber = ""

    def __str__(self):
        return ("Customer {name = '" +self.__name + "', id = '" +str(self.__id))