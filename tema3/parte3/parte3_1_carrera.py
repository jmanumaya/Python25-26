import threading
import random
import time

barrera = threading.Barrier(10)

class Corredor(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} esta en la linea de salida")
        barrera.wait()

        if self.name == "Corredor-0":
            for i in range(3, 0, -1):
                print(f"Cuenta atras: {i}")
                time.sleep(1)
            print("PISTOLATAZO DE SALIDA!")
            barrera.reset()

        barrera.wait()

        inicio = time.time()
        tiempo_carrera = random.uniform(5, 15)
        time.sleep(tiempo_carrera)
        fin = time.time()
        print(f"{self.name} ha terminado la carrera en {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    hilos = [Corredor(f"Corredor-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
