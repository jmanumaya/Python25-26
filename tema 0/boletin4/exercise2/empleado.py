class Empleado():

    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def __str__(self):
        return f"Empleado: {self.nombre}"
        