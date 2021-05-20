from State import State
from State1 import State1
class Calculater():
    def __init__(self):
        self.State = State1()
        self.n1=None
        self.n2=None
        self.operator=None

    def setState(self,State):
        self.State = State

    def addDigit(self,digit):
        resultDigit=[]
        resultDigit.append(digit)

    def inputOperator(self,operator):
        self.operator=operator

    def calculate(self):
        pass
