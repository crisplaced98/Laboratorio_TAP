class Test:

    def test(c):
        for elem in c:
            print(elem)
        print('---------------------------------')

    def test2(c):
        for value in c:
            print(value)
        print('---------------------------------')

    lista = ['uno', 'dos', 'tres', 'cuatro', 'tres']
    c = []
    for value in lista:
        c.append(value)

    test(c)
    test2(c)    #En Python no es ilegal