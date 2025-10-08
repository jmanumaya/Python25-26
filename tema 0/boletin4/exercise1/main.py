from animal import Animal
from gato import Gato
from perro import Perro

def main():
    # Crear algunos animales
    animal = Animal("Bicho", 6)
    gato = Gato("Michi", 4)
    perro = Perro("Firulais", 4)

    # Mostrar sus descripciones
    print(animal)
    print(gato)
    print(perro)

main()