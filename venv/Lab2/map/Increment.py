from Lab2.map.IMap import IMap
class Increment(IMap):
    def apply(self, elem):
        return elem + 1