from Lab3.solutions_filesystem.File import File
from Lab3.solutions_filesystem.Directory import Directory

class Main:
    root = Directory("root")
    home = Directory("home")
    lp = Directory("lp")
    f1 = File("f1", 1234)
    f2 = File("f2", 3445)
    f3 = File("f3", 6688)
    f4 = File("lp", 99999)

    root.addChild(home)
    root.addChild(f1)
    home.addChild(lp)
    home.addChild(f2)
    lp.addChild(f3)
    root.addChild(f4)

    root.ls()
    print("---------------------------")
    result = root.collect()
    for elem in result:
        print(elem)
    '''print("---------------------------")
    result2 = root.search("lp")
    for elem2 in result2:
        print(elem2)
    print("---------------------------")
    print(f3)
    print("---------------------------")

    result3 = root.toList()
    for a in result3:
        print(a)

    print("---------------------------")
    print("root SIZE: " +str(root.size()))
    print("home SIZE: " +str(home.size()))
    print("lp SIZE: " +str(lp.size()))'''