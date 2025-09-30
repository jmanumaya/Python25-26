# Realiza un programa que pida 8 números enteros y los almacene en una lista. 
# A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

numbers = []

# Promp the user 10 numbers
for _ in range(8): 
    num = int(input("Please enter a number: ")) 
    numbers.append(num)

for i in range(len(numbers)):
    iteration = numbers[i]
    if (iteration % 2 == 0):
        print(f"{iteration} is even")
    else:
        print(f"{iteration} is odd")

