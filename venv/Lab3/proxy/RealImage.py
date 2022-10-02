from Lab3.proxy.Image import Image
class RealImage(Image):
    def __init__(self, filename):
        self.__fileName = filename
        self.loadFromDisk(filename)
    
    def display(self):
        print("Displaying " +str(self.__fileName))
    
    def loadFromDisk(self, fileName):
        print("Loading " +str(self.__fileName))