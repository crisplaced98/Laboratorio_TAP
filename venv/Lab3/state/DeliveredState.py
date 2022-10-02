from Lab3.state.PackageState import PackageState
from Lab3.state import ReceivedState
class DeliveredState(PackageState):
    def next(self, pkg):
        pkg.state = ReceivedState.ReceivedState()
    def prev(self, pkg):
        pkg.state = OrderedState.OrderedState()
    def printStatus(self):
        print("Package delivered to post office, not received yet")
    def __str__(self):
        return "DeliveredState{}"