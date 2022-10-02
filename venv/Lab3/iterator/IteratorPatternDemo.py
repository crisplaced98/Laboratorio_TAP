from Lab3.iterator.NameRepository import NameRepository
class IteratorPatternDemo:
    namesRepository = NameRepository()
    for elem in namesRepository:
        print("Name : " + str(elem))