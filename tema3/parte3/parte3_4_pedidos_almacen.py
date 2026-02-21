import threading
import random
import time

NUM_TRABAJADORES = 5
barrera = threading.Barrier(NUM_TRABAJADORES)
evento_pedido = threading.Event()

class Trabajador(threading.Thread):
    def __init__(self, nombre, num_pedidos):
        threading.Thread.__init__(self, name=nombre)
        self.num_pedidos = num_pedidos

    def run(self):
        print(f"{self.name} listo para empezar")
        barrera.wait()
        print(f"{self.name} comienza a trabajar")

        for _ in range(self.num_pedidos):
            print(f"{self.name} esperando un pedido")
            evento_pedido.wait()
            evento_pedido.clear()
            print(f"{self.name} esta preparando el pedido")
            time.sleep(random.uniform(1, 4))
            print(f"{self.name} ha terminado el pedido")

class GeneradorPedidos(threading.Thread):
    def __init__(self, total_pedidos):
        threading.Thread.__init__(self, name="Generador")
        self.total_pedidos = total_pedidos

    def run(self):
        for i in range(self.total_pedidos):
            time.sleep(random.uniform(2, 5))
            print(f"Nuevo pedido generado ({i + 1}/{self.total_pedidos})")
            evento_pedido.set()

if __name__ == "__main__":
    NUM_PEDIDOS = 3
    trabajadores = [Trabajador(f"Trabajador-{i}", NUM_PEDIDOS) for i in range(NUM_TRABAJADORES)]
    generador = GeneradorPedidos(total_pedidos=NUM_TRABAJADORES * NUM_PEDIDOS)

    generador.start()
    for t in trabajadores:
        t.start()

    generador.join()
    for t in trabajadores:
        t.join()
    print("Todos los pedidos han sido procesados")
