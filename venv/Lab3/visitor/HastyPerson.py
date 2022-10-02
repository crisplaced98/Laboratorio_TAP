# Concrete Element

from Lab3.visitor.Person import Person


class HastyPerson(Person):
    def __init__(self, clockFrequency):
        super().__init__()
        self.__clockFrequency = clockFrequency  # How often he looks at his clock

    def accept(self, v):
        v.visitHasty(self)

    def veryHasty(self):
        return self.__clockFrequency > 4