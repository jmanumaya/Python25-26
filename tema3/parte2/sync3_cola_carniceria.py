import threading
import random
import time

class Cliente(threading.Thread):
    semaforo = threading.Semaphore(4)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} esta esperando en la cola de la carniceria")
        Cliente.semaforo.acquire()
        print(f"El cliente {self.name} esta siendo atendido")
        time.sleep(random.randint(1, 10))
        print(f"El cliente {self.name} ha terminado en la carniceria")
        Cliente.semaforo.release()

if __name__ == "__main__":
    hilos = [Cliente(f"Cliente-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
