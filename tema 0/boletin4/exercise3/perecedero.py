from producto import Producto

class Perecedero(Producto):
    
    def __init__(self, nombre, precio, dias_caduca):
        super().__init__(nombre, precio)
        self.dias_caduca = dias_caduca

    def calcular(self, cantidad):
        match(self.dias_caduca):
            case 1:
                res = super().calcular(cantidad) / 4
            case 2:
                res = super().calcular(cantidad) / 3
            case 3:
                res = super().calcular(cantidad) / 2
            case _:
                res = super().calcular(cantidad)
        return res
    
    def __str__(self):
        return f"{super().__str__()}, caduco en: {self.dias_caduca} dias"