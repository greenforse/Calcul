from State1 import State1
from State import State

class State2(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.setState(State1(self.calculator)) 

    def input_operation(self, operator):
        self.calculator.addOperator(operator)

    def input_equals(self):
        self.calculator.calculate()
        self.calculator.outputresult()