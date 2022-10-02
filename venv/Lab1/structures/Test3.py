from Lab1.structures.Client import Client

class Test3:
    def prints(c):
        for p in c:
            print("name: " +str(p.name)+ " age: " +str(p.age))
        print("-------------------------")

    p1 = Client("jose", 30)
    p2 = Client("pedro", 24)
    p3 = Client("jcarlos", 100)

    c = list((p1, p2, p3))

    print("-No ordering---------------")
    prints(c)

    '''En python no se utiliza el Collections.sort. Para ordenar por una variable se utiliza el sort'''
    c.sort(key=lambda x: x.name)
    print("-Ordered by name--------");
    prints(c)

    c.sort(key=lambda x: x.age)
    print("-Ordered by age--------")
    prints(c)

