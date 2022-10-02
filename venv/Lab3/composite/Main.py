from Lab3.composite.File import File
from Lab3.composite.Directory import Directory

class Main:
    root = Directory("root")
    home = Directory("home")
    tap = Directory("tap")
    f1 = File("f1", 1234)
    f2 = File("f2", 3445)
    f3 = File("f3", 6688)
    f4 = File("f4", 99999)

    root.addChild(home)
    root.addChild(f1)
    home.addChild(tap)
    home.addChild(f2)
    tap.addChild(f3)
    root.addChild(f4)

    print("---------------------------")
    print("root SIZE: " +str(root.size()))
    print("home SIZE: " +str(home.size()))
    print("TAP SIZE: " +str(tap.size()))