# Concrete Element
from Lab3.visitor.TaxiVisitor import TaxiVisitor
from Lab3.visitor.HastyPerson import HastyPerson
from Lab3.visitor.LeisurelyPerson import LeisurelyPerson


class HonoredTaxiVisitor(TaxiVisitor):
    def visitHasty(self, e):
        if e.veryHasty():
            print(f'I drive as fast as I can')
        else:
            print(f'I drive fast')

    def visitLeisurely(self, e):
        print(f'I drive in a natural way')