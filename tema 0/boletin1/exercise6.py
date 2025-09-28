# Pedir un número y calcular su factorial. 
# Por ejemplo, el factorial de 5 se denota 5! 
# y es igual a 5x4x3x2x1 = 120.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Please enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
