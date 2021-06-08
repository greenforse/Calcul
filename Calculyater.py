import FirstDigitInputState as f
class Calculater():
    def __init__(self):
        self.State = f.State1(self)
        self.n1=None
        self.n2=None
        self.operator=None
        self.resultDigit=[]
        self.result=None

    def setState(self,State):
        self.State = State

    def addDigit(self,digit):
        #self.resultDigit=[]
        self.resultDigit.append(int(digit))
        #print(self.resultDigit)
        self.outputDigit()
    
    def perevodVintn1(self):
        self.n1=self.perevodVint()

    def perevodVintn2(self):
        self.n2=self.perevodVint()

    def perevodVint(self):
        res=0
        for i in range(len(self.resultDigit)):
            res+=self.resultDigit[i]*(10**(len(self.resultDigit)-i))
        self.resultDigit=[]
        return int(res/10)

    def addOperator(self,operator):
        print("Добавили операцию")
        self.operator=operator

    def calculate(self):
        if self.operator=="+":
            self.result = self.n1 + self.n2
        elif self.operator=="-":
            self.result = self.n1 - self.n2
        elif self.operator=="*":
            self.result = self.n1 * self.n2  
        elif self.operator=="/":
            self.result = self.n1 // self.n2

    def input_digit(self, digit):
        self.State.input_digit(digit)

    def input_operation(self, operator):
        print("Ввели операцию")
        self.State.input_operation(operator)
        print("Ввели операцию")

    def input_equals(self):
        self.State.input_equals()
    
    def outputDigit(self):
        for i in range(len(self.resultDigit)):
            print (self.resultDigit[i],end="")

    def outputresult(self):
        print(self.result)
        self.n1=self.result
        self.result=None