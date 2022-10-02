from Lab3.solutions_visitor.File import File
from Lab3.solutions_visitor.Directory import Directory
from Lab3.solutions_visitor.SizeVisitor import SizeVisitor


class Main:
    root = Directory("root")
    home = Directory("home")
    lp = Directory("lp")
    f1 = File("f1", 1234, "pedro")
    f2 = File("f2", 3445, "pep")
    f3 = File("f3", 6688, "pedro")
    f4 = File("lp", 99999, "jordi")

    root.addChild(home)
    root.addChild(f1)
    home.addChild(lp)
    home.addChild(f2)
    lp.addChild(f3)
    root.addChild(f4)

    root.ls()
    print("---------------------")

    print(f3)
    print("---------------------")

    result3 = root.toList()
    for a in result3:
        print(a)

    print("Visitor code:------size")
    vs = SizeVisitor()
    root.accept(vs)
    print(vs.getsize())