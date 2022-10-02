from Lab3.observer.Observer import Observer
class BinaryObserver(Observer):
    def update(self, newValue):
        print("Binary String: " +str(bin(newValue)))
