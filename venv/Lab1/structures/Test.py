from collections import deque
class Test:
    def test(c):
        strings = ['uno', "dos", "tres", "cuatro", "tres"]
        for num in strings:
            if (isinstance(c, set)):
                c.add(num)
            else:
                c.append(num)

        for num in c:
            print(num)
        print("-------------------------")
    #En Python una List es como una ArrayList ya que no tiene límite de espacio
    c = []
    test(c)

    #En Pyhton una LinkedList es un deque
    c = deque()
    test(c)

    c = set()
    test(c)