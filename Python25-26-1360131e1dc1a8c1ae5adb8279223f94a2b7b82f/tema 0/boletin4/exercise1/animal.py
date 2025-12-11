class Animal:

    def __init__(self, nombre, numPatas):
        self.nombre = nombre
        self.numPatas = numPatas

    def habla(self): 
        return ""

    def __str__(self): 
        return f"Me llamo {self.nombre} tengo {self.numPatas} y sueno así: {self.habla()}"