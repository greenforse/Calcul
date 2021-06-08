from State import State
import SecondDigitInputState as s
import ResultState as r

class State2(State):
    def __init__(self, calculator):
        self.calculator = calculator

    def input_digit(self, digit):
        self.calculator.addDigit(digit)
        self.calculator.setState(s.State3(self.calculator))

    def input_operation(self, operator):
        self.calculator.addOperator(operator)

    def input_equals(self):
        self.calculator.autoZapolnenieN2()
        self.calculator.calculate()
        self.calculator.outputresult()
        self.calculator.setState(r.State4(self.calculator))