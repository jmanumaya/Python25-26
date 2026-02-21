import threading
import random
import time

class Cliente(threading.Thread):
    sem_carniceria = threading.Semaphore(4)
    sem_charcuteria = threading.Semaphore(2)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def ir_carniceria(self):
        print(f"{self.name} esperando en carniceria")
        Cliente.sem_carniceria.acquire()
        print(f"{self.name} esta siendo atendido en carniceria")
        time.sleep(random.randint(1, 5))
        print(f"{self.name} ha terminado en carniceria")
        Cliente.sem_carniceria.release()

    def ir_charcuteria(self):
        print(f"{self.name} esperando en charcuteria")
        Cliente.sem_charcuteria.acquire()
        print(f"{self.name} esta siendo atendido en charcuteria")
        time.sleep(random.randint(1, 5))
        print(f"{self.name} ha terminado en charcuteria")
        Cliente.sem_charcuteria.release()

    def run(self):
        if random.random() < 0.5:
            self.ir_carniceria()
            self.ir_charcuteria()
        else:
            self.ir_charcuteria()
            self.ir_carniceria()
        print(f"{self.name} ha sido completamente atendido")

if __name__ == "__main__":
    hilos = [Cliente(f"Cliente-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
