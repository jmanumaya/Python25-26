from producto import Producto

class No_perecedero(Producto):
    
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular(self, cantidad):
        return super().calcular(cantidad)
    
    def __str__(self):
        return f"{super().__str__()}, tipo: {self.tipo}"