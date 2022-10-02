from Lab2.solutions_accounts.AccType import AccType
class Account:
    def __init__(self, id, name, type, balance):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    @property
    def type(self):
        return self.__type

    def deposit(self, money):
        self.__balance += money
        return (self)

    def __str__(self):
        return ("Account{ name = '" +str(self.__name)+"', balance = " +str(self.__balance)+ ", type = " +str(self.__type) +"}")