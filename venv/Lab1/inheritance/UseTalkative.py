from Lab1.inheritance.Talkative import Talkative
from Lab1.inheritance.Bart import Bart
from Lab1.inheritance.Homer import Homer

class UseTalkative:
    homer = Homer()
    bart = Bart()
    springfield = [homer, bart]

    for h in springfield:
        print(h.talk())