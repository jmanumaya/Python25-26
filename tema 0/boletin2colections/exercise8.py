# Diseña un programa que registre las ventas de una tienda en un diccionario, 
# donde las claves son los nombres de los productos y los valores son las cantidades vendidas. 
# El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto específico. 
# Implementa un menú con ambas opciones. 

inventary = {}

print("INVENTARY\n1. Add Sales\n2. Calculate Total Sales of the Product\n0. Exit")
choice = int(input("Please enter a choice: "))

while choice != 0:
    match choice:
        case 1:
            print("Add Sales")
            name = input("Please enter the name: ")
            amount = int(input("Please Amount Sales: "))
            inventary[name] += amount
        case 2:
            print("Calculate Total Sales of the Product")
            name = input("Please enter the name: ")
            print(inventary.get(name))
        case 0:
            print("Saliendo...")
        case _:
            print("Choise Invalid.")

    print("AGENDA\n1. Add Sales\n2. Calculate Total Sales of the Product\n0. Exit")
    choice = int(input("Please enter a choice: "))

print("END")