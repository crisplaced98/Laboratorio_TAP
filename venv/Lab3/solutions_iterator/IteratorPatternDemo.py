from Lab3.solutions_iterator.NameRepository import NameRepository
class IteratorPatternDemo:
    namesRepository = NameRepository()
    for elem in namesRepository:
        print("Name : " + str(elem))