import unittest
from Lab4.calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def testAdd(self):
        value1 = 3
        value2 = 3
        result = value1 + value2
        print("-> TESTING ADD...")
        c = Calculator()
        self.assertTrue(c.add(value1, value2) == result)

    def testSubtract(self):
        value1 = 5
        value2 = 10
        result = value1 - value2
        print("-> TESTING SUBTRACT...")
        c = Calculator()
        self.assertTrue(c.subtract(value1, value2) == result)
    def testMultiply(self):
        value1 = 3
        value2 = 4
        result = value1 *value2
        print("-> TESTING MULTIPLY...")
        c = Calculator()
        self.assertTrue(c.multiply(value1, value2) == result)
    def testDivide(self):
        value1 = 9
        value2 = 12
        result = value1 /  value2
        print("-> TESTING Divide...")
        c = Calculator()
        self.assertTrue(c.divide(value1, value2) == result)

if __name__ == '__main__':
    unittest.main()
