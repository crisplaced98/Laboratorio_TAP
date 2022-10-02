from Lab3.visitor.TaxiVisitor import TaxiVisitor
from Lab3.visitor.HastyPerson import HastyPerson
from Lab3.visitor.LeisurelyPerson import LeisurelyPerson


class CorruptTaxiVisitor(TaxiVisitor):
    def visitHasty(self, e):
        if e.veryHasty():
            print(f'I drive slowly. Clink click clink...')
        else:
            print(f'I drive very slowly. Clink clink clink...')
    def visitLeisurely(self, e):
        if e.bigSmile():
            print('I drive as slowly as I can. Clink clink clink...')
        else:
            print(f'I drive very slowly. Clink clink clink...')