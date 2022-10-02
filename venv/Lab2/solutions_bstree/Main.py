from Lab2.solutions_bstree.BSTree import BSTree
from Lab2.solutions_bstree.Comparaint import Comaparaint

class Main:
    arbol = BSTree(Comaparaint())
    arbol.insert(5)
    arbol.insert(3)
    arbol.insert(6)
    arbol.insert(1)
    arbol.insert(4)
    print(arbol.contains(4))
    print(arbol.contains(8))
    print(BSTree.tree2List(arbol))