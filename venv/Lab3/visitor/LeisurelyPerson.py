# Concrete Element
from Lab3.visitor.Person import Person


class LeisurelyPerson(Person):
    def __init__(self, smile):
        super()
        self.__smile = smile  # How big is his smile

    def accept(self, v):
        v.visitLeisurely(self)

    def bigSmile(self):
        return self.__smile > 5