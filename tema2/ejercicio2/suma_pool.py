from multiprocessing import Pool
import time

def sumar_hasta(n):
    # Calcula la suma y la imprime (como pide el enunciado)
    resultado = sum(range(1, n + 1))
    print(f"Resultado: {resultado}")
    return resultado

if __name__ == '__main__':
    limite = int(input("Introduce el número: "))
    
    # Preparamos una lista con los valores para los procesos
    # Por ejemplo, lanzamos 3 procesos con el mismo número
    datos = [limite, limite, limite]
    
    inicio = time.time()

    # Usamos el Pool con 3 procesos según tus apuntes
    with Pool(processes=3) as pool:
        pool.map(sumar_hasta, datos)

    final = time.time()

    print(f"Todos los procesos han terminado.")
    print(f"Tiempo total: {final - inicio:.4f} segundos")