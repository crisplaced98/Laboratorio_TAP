from Lab3.observer.Subject import Subject
from Lab3.observer.HexaObserver import HexaObserver
from Lab3.observer.OctalObserver import OctalObserver
from Lab3.observer.BinaryObserver import BinaryObserver

class Test:
    subject = Subject()

    subject.attach(HexaObserver())
    subject.attach(OctalObserver())
    subject.attach(BinaryObserver())

    print("First state change: 15")
    subject.state = 15

    print("Second state change: 10")
    subject.state = 10