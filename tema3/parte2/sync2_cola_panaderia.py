import threading
import random
import time

class Cliente(threading.Thread):
    lock = threading.Lock()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} esta esperando en la cola de la panaderia")
        with Cliente.lock:
            print(f"{self.name} esta siendo atendido")
            time.sleep(random.randint(1, 5))
            print(f"{self.name} ha sido atendido y se va")

if __name__ == "__main__":
    hilos = [Cliente(f"Cliente-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
