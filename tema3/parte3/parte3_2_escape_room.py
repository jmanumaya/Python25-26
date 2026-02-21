import threading
import random
import time

codigo_secreto = random.randint(1000, 9999)
evento_encontrado = threading.Event()
barrera = threading.Barrier(5)

class Persona(threading.Thread):
    lock = threading.Lock()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} empieza a buscar la clave")
        while not evento_encontrado.is_set():
            intento = random.randint(1000, 9999)
            with Persona.lock:
                if not evento_encontrado.is_set() and intento == codigo_secreto:
                    evento_encontrado.set()
                    print(f"{self.name} ha encontrado la clave: {intento}")
                    return

        print(f"{self.name} sabe que la clave fue encontrada, se dirige a la salida")
        barrera.wait()
        print(f"{self.name} sale de la sala junto al grupo")

if __name__ == "__main__":
    print(f"Codigo secreto: {codigo_secreto}")
    hilos = [Persona(f"Persona-{i}") for i in range(5)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print("Todos han salido del Escape Room")
