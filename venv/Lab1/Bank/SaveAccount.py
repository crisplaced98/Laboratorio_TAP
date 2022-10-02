from Lab1.Bank.Account import Account
class SaveAccount(Account):
    def __init__(self, balance, owner):
        super(SaveAccount, self).__init__(balance, owner)
        self.interest = 0.2