from Lab3.state.PackageState import PackageState

class ReceivedState(PackageState):
    def next(self, pkg):
        print("This package is already received by a client")
    def prev(self, pkg):
        pkg.state = DeliveredState()
    def printStatus(self):
        print("Package was received by client")
    def __str__(self):
        return "ReceivedState{}"