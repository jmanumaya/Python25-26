from multiprocessing import Process
import time

def sumar_hasta(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"Resultado de la suma hasta {n}: {suma}")

if __name__ == "__main__":
    valor = int(input("Introduce el número límite: "))
    
    tiempo_inicio = time.time()

    p1 = Process(target=sumar_hasta, args=(valor,))
    p2 = Process(target=sumar_hasta, args=(valor,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    tiempo_final = time.time()

    print("Todos los procesos han terminado.")
    print(f"Tiempo total: {tiempo_final - tiempo_inicio:.4f} segundos")