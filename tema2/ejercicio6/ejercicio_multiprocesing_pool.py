from multiprocessing import Pool
import time

def sumar_rango(a, b):
    """
    Suma todos los números entre a y b (ambos incluidos).
    """
    inicio = min(a, b)
    fin = max(a, b)
    
    resultado = sum(range(inicio, fin + 1))
    
    print(f"Proceso (args: {a}, {b}) -> Suma entre {inicio} y {fin}: {resultado}")
    return resultado

if __name__ == '__main__':
    datos = [
        (1, 10), 
        (10, 1), 
        (5, 5), 
        (50, 60),
        (100, 200)
    ]

    print("--- Iniciando el Pool de procesos ---")

    with Pool() as pool:
        pool.starmap(sumar_rango, datos)

    print("--- Todos los procesos han terminado ---")