# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

# Promp the user a number.
number = int(input("Please enter a number: "))

# Use a for-each to show in the screen the numbers range of 1 to choseen for user
for number in range(1, number + 1):
    print(number)