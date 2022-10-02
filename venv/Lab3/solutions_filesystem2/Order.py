#En Python en vez de crear una clase lo definiría en el AComponent y override el __eq__
class Order:
    def compare(self, other):
        return (self.getName() == other.getName())