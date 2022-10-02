from Lab1.Bank.Customer import Customer
from Lab1.Bank.NoMoney import NoMoney
class Account:
    def __init__(self, balance, owner):
        self._balance = balance
        self.__owner = owner
        self.__interest = 0

    def deposit(self, amount):
        self._balance = self._balance + amount

    def __str__(self):
        return ("Account{ balance = " +str(self._balance) + ", owner = " + str(self.__owner) + "}")


    def revision(self):
        self._balance = self.balance + self.balance*self.interest - self.getComission()

    def withdraw(self, amount):
        if(amount > self._balance):
            raise NoMoney("No money enough")
        else:
            self._balance = self._balance - amount
    
    def getComission(self):
        return 1

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, interest):
        self.__interest = interest