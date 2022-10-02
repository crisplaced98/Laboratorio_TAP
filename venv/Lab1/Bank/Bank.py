from Lab1.Bank.Account import Account
from Lab1.Bank.Customer import Customer
from collections import deque
class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = deque()
        self.__customers = deque()

    def addAccount(self, newAccount):
        self.__accounts.append(newAccount)

    def removeAccount(self, oldAccount):
        self.__accounts.remove(oldAccount)

    def addCustomer(self, newCustomer):
        self.__customers.append(newCustomer)

    def removeCustomer(self, oldCustomer):
        self.__customers.remove(oldCustomer)

    @property
    def customers(self):
        return self.__customers

    @property
    def accounts(self):
        return self.__accounts

    def showAccounts(self):
        for a in self.__accounts:
            print(a)

    def revision(self):
        for acc in self.__accounts:
            acc.revision()
