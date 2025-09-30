# Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

import random

numeros = []
for _ in range(10):
    numeros.append(random.randint(1, 100))

print(numeros)
