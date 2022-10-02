from Lab2.solutions_bstree2.BSTree import BSTree

class Main:
    arbol = BSTree()
    arbol.insert(5)
    arbol.insert(3)
    arbol.insert(6)
    arbol.insert(1)
    arbol.insert(4)
    print(arbol.contains(4))
    print(arbol.contains(8))
    print(BSTree.tree2List(arbol))