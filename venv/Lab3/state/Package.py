from Lab3.state import OrderedState
class Package:
    __state = OrderedState.OrderedState()
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
    def previousState(self):
        self.__state.prev(self)
    def nextState(self):
        self.__state.next(self)
    def printStatus(self):
        self.__state.printStatus()