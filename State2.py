from State3 import State3
from State import State
from State4 import State4

class State2(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.setState(State3(self.calculator))

    def input_operation(self, operator):
        self.calculator.addOperator(operator)

    def input_equals(self):
        self.calculator.setState(State4(self.calculator))