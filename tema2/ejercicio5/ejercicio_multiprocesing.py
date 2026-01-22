from multiprocessing import Process

def sumar_rango(a, b):
    """
    Suma todos los números entre a y b (ambos incluidos).
    Maneja el caso de que a sea mayor que b.
    """
    inicio = min(a, b)
    fin = max(a, b)

    resultado = sum(range(inicio, fin + 1))
    
    print(f"Proceso (args: {a}, {b}) -> Suma entre {inicio} y {fin}: {resultado}")

if __name__ == '__main__':
    procesos = []

    datos = [
        (1, 10),
        (10, 1),
        (5, 5),
        (50, 60)
    ]

    print("--- Iniciando procesos ---")

    for n1, n2 in datos:
        p = Process(target=sumar_rango, args=(n1, n2))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("--- Todos los procesos han terminado ---")