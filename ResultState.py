from State import State
from FirstDigitInputState import State1

class State4(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.addDigit(digit)
        self.calculator.setState(State1(self.calculator)) 

    def input_operation(self, operator):
        self.calculator.addOperator(operator)

    def input_equals(self):
        self.calculator.calculate()
        self.calculator.outputresult()