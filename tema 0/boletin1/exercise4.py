# Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 
# (generado aleatoriamente). Para ello se introduce por teclado una serie de números, 
# para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. 
# El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).

# import a random class for can use in this exercise
import random

# Have a secret number
aleatory = random.randint(1, 100)

# Promp the user a number for try know the secret number.
number = int(input("Please try know the secret number: "))

# Use a "while" for check if the user know a secret number or he have giver up.
while number != aleatory and number != -1:
    print("Your number is higher than the secret number.") if number > aleatory else print("Your number is less than the secret number.")
    number = int(input("Please try know the secret number: "))

# Show in the screen the final result of the program.
if number != -1:
    print(f"Congratulations!!! You discover the secret number 🎉: {aleatory}")
else:
    print(f"Ohh, you have given up... The secret number was {aleatory}")