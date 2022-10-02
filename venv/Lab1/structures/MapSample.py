from Lab1.structures.Person import Person
class MapSample:
    p1 = Person("111", "pedro", 1)
    p2 = Person("222", "pep", 2)
    p3 = Person("333", "pere", 3)

    #En Python utilizamos diccionarios en vez de Map
    persons = {p1.dni:p1, p2.dni: p2}
    persons[p3.dni] = p3

    print(persons.get('222'))

