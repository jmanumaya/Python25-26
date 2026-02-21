import threading
import random
import time
import queue

# Cola con capacidad maxima de 1 elemento
# Para cambiar a 5 elementos, cambia MAX_COLA = 5
MAX_COLA = 1

cola = queue.Queue(maxsize=MAX_COLA)
cond = threading.Condition()

class Productor(threading.Thread):
    def __init__(self, nombre, num_items):
        threading.Thread.__init__(self, name=nombre)
        self.num_items = num_items

    def run(self):
        for i in range(self.num_items):
            dato = f"dato-{self.name}-{i}"
            with cond:
                while cola.full():
                    print(f"{self.name} esperando, la cola esta llena")
                    cond.wait()
                cola.put(dato)
                print(f"{self.name} ha producido: {dato} (cola: {cola.qsize()}/{MAX_COLA})")
                cond.notify_all()
            time.sleep(random.uniform(0.5, 2))

class Consumidor(threading.Thread):
    def __init__(self, nombre, num_items):
        threading.Thread.__init__(self, name=nombre)
        self.num_items = num_items

    def run(self):
        for _ in range(self.num_items):
            with cond:
                while cola.empty():
                    print(f"{self.name} esperando, la cola esta vacia")
                    cond.wait()
                dato = cola.get()
                print(f"{self.name} ha consumido: {dato} (cola: {cola.qsize()}/{MAX_COLA})")
                cond.notify_all()
            time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    NUM_ITEMS = 5
    productor = Productor("Productor-1", NUM_ITEMS)
    consumidor = Consumidor("Consumidor-1", NUM_ITEMS)

    productor.start()
    consumidor.start()

    productor.join()
    consumidor.join()
    print("Produccion y consumo completados")

# PREGUNTA: ¿Cambiaria mucho la solucion si el maximo son 5 elementos?
#   No cambiaria la estructura. Solo hay que modificar MAX_COLA = 5.
#   La logica de espera con Condition es identica: el productor espera si
#   la cola esta llena y el consumidor espera si esta vacia. Con cola de 5,
#   el productor puede adelantarse mas al consumidor antes de bloquearse,
#   lo que reduce la frecuencia de esperas y mejora el rendimiento.
