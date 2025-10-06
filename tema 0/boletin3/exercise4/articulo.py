class Articulo:

    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 0.21
        self.cuantosQuedan = cuantosQuedan

    def getPVP(self): return self.precio * self.IVA

    def getPVPDescuento(self, descuento): return (self.precio * self.IVA) - descuento

    def vender(self, cantidad): 
        res = False
        if self.cuantosQuedan >= cantidad:
            res = True
            self.cuantosQuedan -= cantidad
        return res
    
    def almacenar(self, cantidad):
        self.cuantosQuedan + cantidad

    def __str__(self): return f"Articulo: {self.nombre}, con precio: {self.precio}, quedan: {self.cuantosQuedan} unidades"

    def __eq__(self, other): return self.nombre == other.nombre
    
    def __lt__(self, other): return self.nombre < other.nombre