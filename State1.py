from State import State
class State1(State):

    def input_digit(self, digit):
        while digit !="+" or digit !="-" or digit != "*" or digit !="/" or digit!="=":
            self.calculator.addDigit(digit)
        if digit = "=":
            self.calculator.calculate()
        else:
            self.calculator.setState(State2(self.calculator))