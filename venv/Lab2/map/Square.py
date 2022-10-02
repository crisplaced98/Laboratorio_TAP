from Lab2.map.IMap import IMap
class Square(IMap):
    def apply(self, elem):
        return elem * elem