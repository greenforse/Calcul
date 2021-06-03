from State import State
import OperantInputState as o
import ResultState as r

class State1(State):

    def input_digit(self, digit):
        self.calculator.addDigit(digit)

    def input_operations(self,operator):
        self.calculator.perevodVintn1()
        self.calculator.addOperator(operator)
        self.calculator.setState(o.State2(self.calculator))

    def input_equals(self):
        self.calculator.setState(r.State4(self.calculator))
