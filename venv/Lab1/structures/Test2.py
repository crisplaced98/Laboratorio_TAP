class Test2:
    def prints(c):
        for num in c:
            print(num)
        print("-------------------------")

    lista = ["uno", "dos", "tres", "cuatro"]
    c = []

    for num in lista:
        c.append(num)
    prints(c)
    c.sort()
    prints(c)
