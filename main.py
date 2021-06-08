from Calculyater import Calculater
calk=Calculater()
while True:
    calkInput=(input("> "))
    try:
        calk.input_digit(calkInput)
    except ValueError:
        if calkInput == "+" or calkInput=="-" or calkInput=="*" or calkInput =="/":
            print("мы попали в плюс")
            calk.input_operation(calkInput)
        elif calkInput == "=":
            print("ввели равно")
            calk.input_equals()
        else: print("Мы не попадаем в условие")