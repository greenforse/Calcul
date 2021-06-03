from State import State
from OperantInputState import State2
from ResultState import State4

class State1(State):

    def input_digit(self, digit):
        self.calculator.addDigit(digit)

    def input_operations(self,operator):
        self.calculator.perevodVintn1()
        self.calculator.addOperator(operator)
        self.calculator.setState(State2(self.calculator))

    def input_equals(self):
        self.calculator.setState(State4(self.calculator))