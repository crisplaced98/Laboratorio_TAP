from Lab3.observer.Observer import Observer
class HexaObserver(Observer):
    def update(self, newValue):
        print("Hex String: " +str(hex(newValue)))