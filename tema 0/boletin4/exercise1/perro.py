from animal import Animal

class Perro(Animal):

    def __init__(self, nombre, numPatas):
        return super().__init__(nombre, numPatas)
    
    def habla(self): return "GUAU"

    def __str__(self):
        return f"Soy un perro {super().__str__()}"