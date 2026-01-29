from multiprocessing import Process, Pipe
import time
import os

def lector(conn):
    """
    Lee el fichero, separa los números y envía la tupla (n1, n2) por la tubería.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, "numeros_pares.txt")
    
    with open(ruta_archivo, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split()
                if len(partes) == 2:
                    n1 = int(partes[0])
                    n2 = int(partes[1])
                    conn.send((n1, n2))
                    
    conn.send(None)
    conn.close()

def sumador(conn):
    """
    Recibe tuplas por la tubería y calcula la suma.
    """
    while True:
        datos = conn.recv()
        
        if datos is None:
            break
            
        a, b = datos
        
        inicio = min(a, b)
        fin = max(a, b)
        resultado = sum(range(inicio, fin + 1))
        
        print(f"Recibido ({a}, {b}) -> Suma entre {inicio} y {fin}: {resultado}")
    
    conn.close()

if __name__ == '__main__':
    izq, der = Pipe()
    
    inicio = time.time()
    print("--- Iniciando procesos con Pipe ---")

    p_lector = Process(target=lector, args=(izq,))
    p_sumador = Process(target=sumador, args=(der,))

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    print("--- Todos los procesos han terminado ---")