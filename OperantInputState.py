from State import State
from SecondDigitInputState import State3
from ResultState import State4

class State2(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.addDigit(digit)
        self.calculator.setState(State3(self.calculator))

    def input_operation(self, operator):
        self.calculator.addOperator(operator)

    def input_equals(self):
        self.calculator.setState(State4(self.calculator))