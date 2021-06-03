from State import State
import FirstDigitInputState as f
import OperantInputState as o
import ResultState as r

class State3(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.addDigit(digit)
        self.calculator.setState(f.State1(self.calculator)) 

    def input_operation(self, operator):
        self.calculator.perevodVintn2()
        self.calculator.calculate()
        self.calculator.outputresult()
        self.calculator.setState(o.State2(self.calculator))
    def input_equals(self):
        self.calculator.perevodVintn2()
        self.calculator.calculate()
        self.calculator.setState(r.State4(self.calculator))