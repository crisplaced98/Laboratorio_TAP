from Lab3.proxy.ProxyImage import ProxyImage
class Main:
    image = ProxyImage("test_10mb.jpg")

    #Image will be loaded from disk
    image.display()
    print("")

    #Image will not be loaded from disk
    image.display()