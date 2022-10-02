from Lab3.visitor.HonoredTaxiVisitor import HonoredTaxiVisitor
from Lab3.visitor.HastyPerson import HastyPerson
from Lab3.visitor.LeisurelyPerson import LeisurelyPerson
from Lab3.visitor.CorruptTaxiVisitor import CorruptTaxiVisitor

class Main:
    taxiDriver = HonoredTaxiVisitor()
    clients = []
    clients.append(HastyPerson(5))
    clients.append(LeisurelyPerson(8))
    for client in clients:
        client.accept(taxiDriver)

    print('---------')

    taxiDriver = CorruptTaxiVisitor()
    for client in clients:
        client.accept(taxiDriver)