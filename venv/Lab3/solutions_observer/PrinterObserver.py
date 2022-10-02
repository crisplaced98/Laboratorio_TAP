from Lab3.solutions_observer.Observer import Observer
class PrinterObserver(Observer):
    def notifyAdd(self, elem):
        print("ADDED: " +str(elem))
    
    def notifyRemove(self, elem):
        print("REMOVED: " +str(elem))

    def __eq__(self, other):
        return type(self).__name__ == type(other).__name__

    def __str__(self):
        return (type(self).__name__)