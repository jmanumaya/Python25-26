import math


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self): return f"({self.x}, {self.y})"

    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, punto): return math.hypot(punto.x - self.x, punto.y - self.y)