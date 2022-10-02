from Lab1.Bank.Customer import Customer
from Lab1.Bank.Account import Account
from Lab1.Bank.Bank import Bank
from Lab1.Bank.SaveAccount import SaveAccount
from Lab1.Bank.CheckingAccount import CheckingAccount
from Lab1.Bank.BonusAccount import BonusAccount
from Lab1.Bank.InvestFund import InvestFund
from Lab1.Bank.NoMoney import NoMoney

class UseBank:
    c1 = Customer("1", "pedro")
    c2 = Customer("2", "pep")
    c3 = Customer("3", "pau")

    a1 = CheckingAccount(90, c1)
    a2 = SaveAccount(100, c2)
    a3 = InvestFund(10, c3)
    a4 = BonusAccount(10, c3)
    
    b1 = Bank("TAP")
    
    b1.addCustomer(c1)
    b1.addCustomer(c2)
    b1.addCustomer(c3)

    b1.addAccount(a1)
    b1.addAccount(a2)
    b1.addAccount(a3)
    b1.addAccount(a4)

    b1.showAccounts()

    a1.deposit(10)

    try:
        a3.withdraw(1)
    except NoMoney as e1:
        print(e1)

    try:
        a4.withdraw(100)
    except NoMoney as e1:
        print(e1)

    print("Before revision")
    b1.showAccounts()
    b1.revision()
    print("After revision")
    b1.showAccounts()