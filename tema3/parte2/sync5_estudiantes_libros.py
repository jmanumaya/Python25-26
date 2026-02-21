import threading
import random
import time

class Estudiante(threading.Thread):
    libros = [True] * 9
    cond = threading.Condition()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            with Estudiante.cond:
                libros_disponibles = [i for i, libre in enumerate(Estudiante.libros) if libre]
                while len(libros_disponibles) < 2:
                    print(f"{self.name} esperando a que haya libros disponibles")
                    Estudiante.cond.wait()
                    libros_disponibles = [i for i, libre in enumerate(Estudiante.libros) if libre]

                elegidos = random.sample(libros_disponibles, 2)
                Estudiante.libros[elegidos[0]] = False
                Estudiante.libros[elegidos[1]] = False
                print(f"{self.name} ha cogido los libros {elegidos[0]} y {elegidos[1]}")

            time.sleep(random.randint(3, 5))

            with Estudiante.cond:
                Estudiante.libros[elegidos[0]] = True
                Estudiante.libros[elegidos[1]] = True
                print(f"{self.name} ha devuelto los libros {elegidos[0]} y {elegidos[1]}")
                Estudiante.cond.notifyAll()
            return

if __name__ == "__main__":
    nombres = ["Ana", "Carlos", "Maria", "Pedro"]
    hilos = [Estudiante(nombre) for nombre in nombres]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print("Todos los estudiantes han utilizado sus libros")
