from Lab2.solutions_accounts.Account import Account
from Lab2.solutions_accounts.AccType import AccType

class Tokens:

    lista = []
    with open("accounts.txt", "r") as fis:
        for x in fis:
            tok = x.replace('\n', ",").split(",")
            if (len(tok) >= 4):
                c = Account(tok[0], tok[1], tok[2], int(tok[3]))
                lista.append(c)
    for acc in lista:
        print(acc)

    print("EXERCISE 1: MAP")
    result = map(lambda x: x.deposit(100), lista)
    for acc in result:
        print(acc)
    print("EXERCISE 2: FILTER")
    result = list(filter( lambda x: (x.type == AccType.IF.value), lista))
    for acc in result:
        print(acc)
    print("EXERCISE 3: MAX")
    print(max(result, key=lambda x: x.balance))


