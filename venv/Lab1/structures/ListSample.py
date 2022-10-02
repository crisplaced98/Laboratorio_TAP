from Lab1.structures.Person import Person
class LisSample:
    p1 = Person("111", "pedro", 1)
    p2 = Person("222", "pep", 2)
    p3 = Person("333", "pere", 3)

    persons = list((p1, p2))
    #La diferencia entre append e insert es que el append lo añade al final de la lista y el insert en un índice
    persons.append(p3)

    for p in persons:
        print(p)

