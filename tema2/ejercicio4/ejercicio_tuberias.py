from multiprocessing import Process, Pipe
import time
import os

def lector(conn):
    """
    Lee el fichero y envía los números por el extremo de la tubería.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, "numeros.txt")
    
    with open(ruta_archivo, "r") as f:
        for linea in f:
            numero = int(linea.strip())
            conn.send(numero)
            
    conn.send(None)
    conn.close()

def sumador(conn):
    """
    Recibe números de la tubería y calcula la suma.
    """
    while True:
        n = conn.recv()
        
        if n is None:
            break
            
        print(f"Suma hasta {n}: {sum(range(1, n + 1))}")
    
    conn.close()

if __name__ == '__main__':
    izq, der = Pipe()
    inicio = time.time()

    p1 = Process(target=lector, args=(izq,)) 
    p2 = Process(target=sumador, args=(der,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    final = time.time()
    print(f"Terminado en: {final - inicio:.4f} segundos")