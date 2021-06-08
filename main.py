from Calculyater import Calculater
calk=Calculater()
while True:
    try:
        calkInput=int(input("> "))
        calk.input_digit(calkInput)
    except:
        calkInput=input("> ")
        if calkInput == "+":
            calk.input_operation(calkInput)
            print("Опять я тупорез")
        if calkInput == "=":
            calk.input_equals()