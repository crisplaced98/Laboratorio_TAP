from Lab3.solutions_observer.ObserverListImpl import ObserverListImpl
from Lab3.solutions_observer.PrinterObserver import PrinterObserver
from Lab3.solutions_observer.BackupObserver import BackupObserver
from Lab3.solutions_observer.RepeatedObserverException import RepeatedObserverException
class Main:
    def testStrings():
        try:
            strings = ObserverListImpl()
            strings.register(PrinterObserver())
            strings.register(BackupObserver())
        except RepeatedObserverException as e:
            print("Existent Observer Exception.....")
            print("  '--------------> " +str(e))

        for s in ["hola", "adios", "hello", "goodbye"]:
            strings.add(s)

        print("List content: ")
        for s in strings:
            print(s)

        print("")
        try:
            strings.register(BackupObserver())
        except RepeatedObserverException as e:
            print("CExixtent Observer... ")
            print("    '--------------> " +str(e))
    def testIntegers():
        try:
            integers = ObserverListImpl()
            integers.register(PrinterObserver())
            integers.register(BackupObserver())
        except RepeatedObserverException as e:
            print("Existent Observer...")
            print("   '----------> " +str(e))

        for s in [4, 6, 3, 5, 4]:
            integers.add(s)

        print("List Content: ")
        for s in integers:
            print(s)

    testStrings()
    testIntegers()