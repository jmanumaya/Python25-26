import threading

class Contador(threading.Thread):
    contador = 0

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while Contador.contador < 1000:
            Contador.contador += 1
            print(f"{self.name} incrementa el contador a {Contador.contador}")

if __name__ == "__main__":
    hilos = [Contador(f"Hilo-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print(f"Valor final del contador: {Contador.contador}")
