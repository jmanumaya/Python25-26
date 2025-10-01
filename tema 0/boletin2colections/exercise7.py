# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones 
# implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. 
# Crea un menú para las distintas opciones e implementa una función para cada opción.

agenda = {}

print("AGENDA\n1. Add Contact\n2. Delete Contact\n3.Search Contact\n0. Exit")
choice = int(input("Please enter a choice: "))

while choice != 0:
    match choice:
        case 1:
            print("Add Contact")
            name = input("Please enter the name: ")
            number = int(input("Please enter her number: "))
            agenda[name] = number
        case 2:
            print("Delete Contact")
            name = input("Please enter the name of the contact to delete")
            del agenda[name]
        case 3:
            print("Search Contact")
            name = input("Please enter the name: ")
            print(agenda.get(name))
        case 0:
            print("Saliendo...")
        case _:
            print("Choise Invalid.")

    print("AGENDA\n1. Add Contact\n2. Delete Contact\n3.Search Contact\n0. Exit")
    choice = int(input("Please enter a choice: "))

print("END")