from Calculyater import Calculater
calk=Calculater()
while True:
    calcInput=input(">")
    #calk.input_digit(calcInput)
    if calcInput != "+" or calcInput !="=":
        calk.input_digit(calcInput)
    elif calcInput == "+":
        calk.input_operation(calcInput)
    elif calcInput == "=":
        calk.input_equals()
    else:
        print("Ничего не подошло")
