from Lab1.Bank.Account import Account
from Lab1.Bank.NoMoney import NoMoney
class InvestFund(Account):
    def __init__(self, balance, owner):
        super(InvestFund, self).__init__(balance, owner)
        self.interest = 0.34
        self.__amount = 0

    def withdraw(self, amount):
        raise NoMoney("InvestFund is locked")
    