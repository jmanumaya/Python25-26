# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

# First, promp the user a number.
numero = int(input("Please enter a number: "))

# And now, show in the screen if the number choseen for the user is even or odd with a ternary
print(f"the number {numero} is even") if numero % 2 == 0 else print(f"the number {numero} is odd")