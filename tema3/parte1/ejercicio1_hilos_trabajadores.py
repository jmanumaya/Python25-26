import threading
import random
import time

class Trabajador(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            time.sleep(random.randint(1, 10))
            print(f"Soy {self.name} y he terminado de trabajar")

if __name__ == "__main__":
    nombres = ["Ana", "Carlos", "Maria", "Pedro", "Laura"]
    hilos = [Trabajador(nombre) for nombre in nombres]
    for hilo in hilos:
        hilo.setDaemon(True)
        hilo.start()
    for hilo in hilos:
        hilo.join()
