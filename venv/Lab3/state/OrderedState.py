from Lab3.state.PackageState import PackageState
from Lab3.state.DeliveredState import DeliveredState

class OrderedState(PackageState):
    def next(self, pkg):
        pkg.state = DeliveredState()
    def prev(self, pkg):
        print("The package is in it's root state")
    def printStatus(self):
        print("Package ordered, not delivered to the office yet")
    def __str__(self):
        return "OrderedSate{}"