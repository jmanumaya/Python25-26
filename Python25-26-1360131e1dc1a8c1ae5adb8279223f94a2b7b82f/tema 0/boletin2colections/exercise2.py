# Crea un programa que pida diez números reales por teclado, los almacene en una lista, 
# y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

numbers = []

# Promp the user 10 numbers
for _ in range(10): 
    num = int(input("Please enter a number: ")) 
    numbers.append(num)

print(f"Max Number: {max(numbers)}, Min Number: {min(numbers)}")

