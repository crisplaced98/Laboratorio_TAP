from Lab3.observer.Observer import Observer
class OctalObserver(Observer):
    def update(self, newValue):
        print("Octal String: " +str(oct(newValue)))