from Lab3.strategy.Strategy import Strategy
class Context:
    def __init__(self, strategy):
        self.__strategy = strategy

    def executeStrategy(self, num1, num2):
        return self.__strategy.doOperation(num1, num2)