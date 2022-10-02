#Adapter (asignación polimorfica)
class UsbToCarAdapter:
    def __init__(self, carInterface):
        self.__carInterface = carInterface

    def getPower(self):
        return self.__carInterface.getEnergy()