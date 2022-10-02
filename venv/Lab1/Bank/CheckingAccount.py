from Lab1.Bank.Account import Account
class CheckingAccount(Account):
    def __init__(self, balance, owner):
        super(CheckingAccount, self).__init__(balance, owner)
        self.interest = 0.1
    
    def revision(self):
        self.balance = self.balance + self.balance*self.interest
    