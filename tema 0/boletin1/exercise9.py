# Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos 
# entre ellos. Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, 
# y pásalos como parámetros de entrada de la función.

# Function that show the range of numbers indicated
def midles_numbers(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)

# Method main that promp the user a range of numbers and call the midles_numbers function
def main():
    num1 = int(input("Please enter a min number: "))
    num2 = int(input("And now, enter the max number: "))
    
    while(num1 > num2):
        num1 = int(input("Please enter a min number: "))
        num2 = int(input("And now, enter the max number: "))

    midles_numbers(num1, num2)

# Start Call of main.
main()