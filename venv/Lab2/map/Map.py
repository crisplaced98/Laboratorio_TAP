class Map:
    def map(lista, function):
        result = []
        a = 0
        for i in lista:
            result.append(function.apply(lista[a]))
            a += 1
        return result
