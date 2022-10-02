from Lab3.solutions_observer.Observer import Observer

class BackupObserver(Observer):
    def __init__(self):
        self.__backup = []

    def notifyAdd(self, elem):
        self.__backup.append(elem)

    def notifyRemove(self, elem):
        self.__backup.remove(elem)

    def __eq__(self, other):
        return type(self).__name__ == type(other).__name__
    def __str__(self):
        return (type(self).__name__)