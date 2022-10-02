from Lab3.strategy.OperationAdd import OperationAdd
from Lab3.strategy.OperationSubstract import OperationSubstract
from Lab3.strategy.OperationMultiply import OperationMultiply
from Lab3.strategy.Context import Context

class Main:
    context = Context(OperationAdd())
    print("10 + 5 = " + str(context.executeStrategy(10, 5)))

    context = Context(OperationMultiply())
    print("10 * 5 = " + str(context.executeStrategy(10, 5)))

    context = Context(OperationSubstract())
    print("10 - 5 = " + str(context.executeStrategy(10, 5)))