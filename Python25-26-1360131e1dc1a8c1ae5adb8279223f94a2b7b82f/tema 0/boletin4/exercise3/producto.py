class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular(self, cantidad):
        return self.precio * cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre}, precio: {self.precio}"
    
    def __lt__(self, other):
        return self.precio < other.precio