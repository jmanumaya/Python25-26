import threading
import random
import time

# Solucion al interbloqueo: el ultimo filosofo coge los palillos en orden inverso
# Esto rompe la circularidad que causaria deadlock

palillos = [threading.Lock() for _ in range(5)]

class Filosofo(threading.Thread):
    def __init__(self, numero):
        threading.Thread.__init__(self, name=f"Filosofo-{numero}")
        self.numero = numero
        self.izquierdo = numero
        self.derecho = (numero + 1) % 5

    def run(self):
        for _ in range(3):
            print(f"{self.name} esta pensando")
            time.sleep(random.uniform(1, 3))

            if self.numero == 4:
                primero, segundo = self.derecho, self.izquierdo
            else:
                primero, segundo = self.izquierdo, self.derecho

            palillos[primero].acquire()
            print(f"{self.name} ha cogido el palillo {primero}")
            palillos[segundo].acquire()
            print(f"{self.name} ha cogido el palillo {segundo} y empieza a comer")

            time.sleep(random.uniform(1, 3))

            palillos[primero].release()
            palillos[segundo].release()
            print(f"{self.name} ha terminado de comer y deja los palillos")

if __name__ == "__main__":
    hilos = [Filosofo(i) for i in range(5)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

# PREGUNTAS:
# ¿Se llega a producir interbloqueo?
#   No. La solucion invierte el orden de cogida de palillos para el filosofo 4,
#   rompiendo la circularidad. Sin esta correccion, todos podrian coger su palillo
#   izquierdo a la vez y quedarse esperando el derecho indefinidamente.
#
# ¿Podria un filosofo no comer nunca?
#   En teoria si, aunque es muy improbable. Si los filosofos adyacentes siempre
#   consiguen los palillos antes que el, podria sufrir inanicion indefinidamente.
#   Esta solucion no garantiza equidad (fairness).
