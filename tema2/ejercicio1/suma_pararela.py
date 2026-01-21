from multiprocessing import Process
import time

# 1. Creamos la función según el enunciado
def sumar_hasta(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"Resultado de la suma hasta {n}: {suma}")

if __name__ == "__main__":
    valor = int(input("Introduce el número límite: "))
    
    # Marcamos el tiempo de inicio
    tiempo_inicio = time.time()

    # 2. Creamos los procesos usando Process(target=..., args=...)
    p1 = Process(target=sumar_hasta, args=(valor,))
    p2 = Process(target=sumar_hasta, args=(valor,))

    # 3. Iniciamos los procesos con start()
    p1.start()
    p2.start()

    # 4. Esperamos a que terminen con join()
    p1.join()
    p2.join()

    # Marcamos el tiempo final
    tiempo_final = time.time()

    print("Todos los procesos han terminado.")
    print(f"Tiempo total: {tiempo_final - tiempo_inicio:.4f} segundos")