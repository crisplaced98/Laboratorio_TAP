from Lab3.solutions_observer.ObserverList import ObserverList
from Lab3.solutions_observer.Observer import Observer
from Lab3.solutions_observer.RepeatedObserverException import RepeatedObserverException

class ObserverListImpl(ObserverList):
    def __init__(self):
        self.__observers = []
        self.__content = []

    def register(self, observer):
        if(observer in self.__observers):
            raise RepeatedObserverException("Observer '" +str(observer)+ "' already exists!")
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

    def notifyAllAdd(self, elem):
        for ob in self.__observers:
            ob.notifyAdd(elem)

    def notifyAllRemove(self, elem):
        for ob in self.__observers:
            ob.notifyRemove(elem)

    def add(self, elem):
        self.__content.append(elem)
        self.notifyAllAdd(elem)

    def remove(self, elem):
        self.__content.remove(elem)
        self.notifyAllRemove(elem)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__content):
            raise StopIteration
        elem = self.__content[self.__index]
        self.__index += 1
        return elem

