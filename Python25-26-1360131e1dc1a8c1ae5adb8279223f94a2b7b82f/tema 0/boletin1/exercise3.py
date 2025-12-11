# Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
# antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.

# Promp the user a number
sum = 0
number = int(input("Please enter a number: "))

# Have a summation with a "while" of the numbers enters for the user while the numbers are positives.
while number >= 0:
    sum = sum + number
    number = int(input("Please enter a number: "))

# Show in the screen the summation of numbers positives.
print(f"Your summation of numbers positive: {sum}")