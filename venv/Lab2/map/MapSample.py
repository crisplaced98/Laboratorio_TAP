from Lab2.map.Increment import Increment
from Lab2.map.Square import Square
from Lab2.map.Map import Map
class MapSample:
    list = [1, 2, 3, 4, 5]
    result = Map.map(list, Increment())
    print(result)

    result = Map.map(list, Square())
    print(result)