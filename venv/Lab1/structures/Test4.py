from Lab1.structures.Client import Client
class Test4:
    p1 = Client("homer", 40)
    p2 = Client("marge", 40)
    p3 = Client("bart", 12)
    p4 = Client("lisa", 10)

    dict = {"dni1": p1, "dni2": p2, "dni3":p3}
    dict["dni4"] = p4

    p = dict.get("dni2")
    print(p.name)

    keys = dict.keys()
    for key in keys:
        x = dict.get(key)
        print(x.name)
    print("-------------------------")

    clients = dict.values()
    for per in clients:
        print(per.name)