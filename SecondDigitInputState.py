from State import State
from FirstDigitInputState import State1
from OperantInputState import State2
from ResultState import State4

class State3(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.addDigit(digit)
        self.calculator.setState(State1(self.calculator)) 

    def input_operation(self, operator):
        self.calculator.perevodVintn2()
        self.calculator.calculate()
        self.calculator.outputresult()
        self.calculator.setState(State2(self.calculator))
    def input_equals(self):
        self.calculator.perevodVintn2()
        self.calculator.calculate()
        self.calculator.setState(State4(self.calculator))