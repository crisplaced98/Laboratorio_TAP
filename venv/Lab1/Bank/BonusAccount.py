from Lab1.Bank.Account import Account
class BonusAccount(Account):
    def __init__(self, balance, owner):
        super(BonusAccount, self).__init__(balance, owner)
        self.interest = 0.6