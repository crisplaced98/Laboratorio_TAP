from Lab2.map2.Map import Map
from Lab2.map2.Increment import Increment
from Lab2.map2.Square import Square
from Lab2.map2.Capitals import Capitals
class MapSample:
    list = [1, 3, 5, 7, 9]
    list2 = ["pedro", "lenguajes", "programacion", "Java", "haskell"]

    result = Map.map(list, Increment())
    print(result)
    result = Map.map(list, Square())
    print(result)
    result = Map.map(list2, Capitals())
    print(result)
