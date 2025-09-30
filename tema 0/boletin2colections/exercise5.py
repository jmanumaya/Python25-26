# Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores 
# enteros aleatorios entre 1 y 10 (utiliza 1 + Math.random()*10). Luego pedirá un valor N y mostrará cuántas veces aparece N. 

import random

numbers = []

# Promp the user 10 numbers
for _ in range(100): 
    numbers.append(random.randint(1, 11))

print(numbers)

n = int(input("Please enter a number of search ocurrences: "))

print(f"{n} have {numbers.count(n)} ocurrences in the list")