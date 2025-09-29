# Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación 
# se desea realizar con ellos. Las operaciones disponibles son sumar, restar, multiplicar o dividir. 
# Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. 
# La función devolverá el resultado de la operación mediante un número real.

def calculator(num1, num2, operator):
    res = 0
    match operator:
        case 1:
            res = num1 + num2
        case 2:
            res = num1 - num2
        case 3:
            res = num1 * num2
        case 4:
            res = num1 / num2
        case _:
            res = "Invalid Operation"
    return res

def main():
    operator_symbols = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
    operator = int(input("And now, enter a number of the operator('1: +, 2: -, 3: /, 4: *'): "))

    if operator in operator_symbols:
        symbol = operator_symbols[operator]
        result = calculator(num1, num2, operator)
        print(f"{num1} {symbol} {num2} = {result}")
    else:
        print("Invalid operator")

main()