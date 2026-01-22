from multiprocessing import Process, Queue
import time
import os

def lector(cola):
    """
    Lee el fichero, separa los dos números de cada línea y 
    los envía como una tupla (n1, n2) a la cola.
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
                    cola.put((n1, n2))
    
    cola.put(None) 

def sumador(cola):
    """
    Recibe tuplas (n1, n2) de la cola y calcula la suma del rango.
    """
    while True:
        datos = cola.get() 
        
        if datos is None:
            break
            
        a, b = datos 
        
        inicio = min(a, b)
        fin = max(a, b)
        
        resultado = sum(range(inicio, fin + 1))
        print(f"Recibido ({a}, {b}) -> Suma entre {inicio} y {fin}: {resultado}")

if __name__ == '__main__':
    cola = Queue()
    inicio = time.time()

    print("--- Iniciando procesos ---")

    p_lector = Process(target=lector, args=(cola,))
    p_sumador = Process(target=sumador, args=(cola,))

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    print("--- Todos los procesos han terminado ---")