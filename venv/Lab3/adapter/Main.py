from Lab3.adapter.CigaretteLighterReceptacle import CigaretteLighterReceptacle
from Lab3.adapter.MP3Player import MP3Player
from Lab3.adapter.UsbToCarAdapter import UsbToCarAdapter
class Main:
    carLighter = CigaretteLighterReceptacle()
    myPlayer = MP3Player('SanDisk', 4, UsbToCarAdapter(carLighter))
    myPlayer.charge()