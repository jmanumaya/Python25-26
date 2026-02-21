import threading
import time
import random

NUM_PEATONES = 8
barrera = threading.Barrier(NUM_PEATONES + 1)

class Peaton(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} esperando en el semaforo")
        barrera.wait()
        print(f"{self.name} esta cruzando la calle")
        time.sleep(random.uniform(1, 3))
        print(f"{self.name} ha cruzado")

class Semaforo(threading.Thread):
    def __init__(self, ciclos):
        threading.Thread.__init__(self, name="Semaforo")
        self.ciclos = ciclos

    def run(self):
        for _ in range(self.ciclos):
            tiempo_rojo = random.randint(3, 6)
            print(f"Semaforo en ROJO durante {tiempo_rojo} segundos")
            time.sleep(tiempo_rojo)
            print("Semaforo en VERDE, peatones pueden cruzar")
            barrera.wait()
            time.sleep(4)

if __name__ == "__main__":
    peatones = [Peaton(f"Peaton-{i}") for i in range(NUM_PEATONES)]
    semaforo = Semaforo(ciclos=3)

    semaforo.start()
    for peaton in peatones:
        peaton.start()

    semaforo.join()
    for peaton in peatones:
        peaton.join()
