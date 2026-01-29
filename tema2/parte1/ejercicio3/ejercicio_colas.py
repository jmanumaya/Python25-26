from multiprocessing import Process, Queue
import time
import os

def lector(cola):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    ruta_archivo = os.path.join(script_dir, "numeros.txt")
    
    with open(ruta_archivo, "r") as f:
        for linea in f:
            cola.put(int(linea.strip())) 
    cola.put(None)

def sumador(cola):
    while True:
        n = cola.get() 
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