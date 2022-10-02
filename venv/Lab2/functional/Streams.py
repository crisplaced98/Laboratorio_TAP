from Lab2.functional.Animal import Animal
class Streams:
    lista = []
    a1 = Animal("loro", 24)
    a2 = Animal("oso", 75)
    a3 = Animal("gato", 16)
    a4 = Animal("perro", 6)
    a5 = Animal("elefante", 67)
    a6 = Animal("mamut", 81)

    lista.append(a1)
    lista.append(a2)
    lista.append(a3)
    lista.append(a4)
    lista.append(a5)
    lista.append(a6)

    result = list((filter(lambda x: (x.age > 30), lista)))
    for elem in result:
        print(elem)
    num = len(list((filter(lambda x: (x.age > 30), lista))))
    print("number: " +str(num))