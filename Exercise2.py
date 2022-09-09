def biggerNumber(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
            return number1

    if number2 > number1:
        if number2 > number3:
            return number2
            
    if number3 > number1:
        if number3 > number2:
            return number3

def run():
    number1 = int(input('Ingrese su Primer:'))
    number2 = int(input('Ingrese su Segundo:'))
    number3 = int(input('Ingrese su Tercer:'))
    result = biggerNumber(number1, number2, number3)
    print(result)

if __name__ == '__main__':
    run()