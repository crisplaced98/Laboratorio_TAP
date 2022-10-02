from Lab3.strategy.Strategy import Strategy
class OperationSubstract(Strategy):
    def doOperation(self, num1, num2):
        return (num1 - num2)