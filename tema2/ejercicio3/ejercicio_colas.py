from multiprocessing import Process, Queue
import time

def lector(cola):
    with open("numeros.txt", "r") as f:
        for linea in f:
            cola.put(int(linea.strip())) # Insertar en cola (Imagen III)
    cola.put(None) # Señal de fin

def sumador(cola):
    while True:
        n = cola.get() # Obtener de cola (Imagen III)
        if n is None:
            break
        print(f"Suma hasta {n}: {sum(range(1, n + 1))}")

if __name__ == '__main__':
    cola = Queue()
    inicio = time.time()

    p1 = Process(target=lector, args=(cola,))
    p2 = Process(target=sumador, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    final = time.time()
    print(f"Terminado en: {final - inicio:.4f} segundos")