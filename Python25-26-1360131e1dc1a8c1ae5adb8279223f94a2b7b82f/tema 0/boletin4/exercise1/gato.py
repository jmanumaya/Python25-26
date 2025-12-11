from animal import Animal

class Gato(Animal):

    def __init__(self, nombre, numPatas):
        return super().__init__(nombre, numPatas)
    
    def habla(self): return "MIAU"

    def __str__(self):
        return f"Soy un gato {super().__str__()}"