# Cliente
class MP3Player:
    def __init__(self, brand, storageCapacity, baterryCharger):
        self.__brand = brand
        self.__storageCapacity = storageCapacity
        self.__batteryChargerInterface = baterryCharger
        self.__batteryLevel = 0

    def charge(self):
        print(f'--- Battery level before: {self.__batteryLevel} ---')
        self.__batteryLevel = self.__batteryLevel + self.__batteryChargerInterface.getPower()
        print(f'--- Battery level after: {self.__batteryLevel} ---')

    @property
    def Brand(self):
        return self.__brand

    @property
    def StorageCapacity(self):
        return self.__storageCapacity