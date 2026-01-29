import multiprocessing
import random
import time

def generar_ips(cola_salida):
    """Proceso 1: Genera IPs y las pone en la cola"""
    for _ in range(10):
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        cola_salida.put(ip)
    cola_salida.put(None)

def filtrar_ips(cola_entrada, cola_salida):
    """Proceso 2: Lee IPs, filtra y envía"""
    while True:
        ip = cola_entrada.get()
        if ip is None:
            cola_salida.put(None)
            break
        
        primer_octeto = int(ip.split('.')[0])
        clase = ""
        
        if 0 <= primer_octeto <= 127: clase = "A"
        elif 128 <= primer_octeto <= 191: clase = "B"
        elif 192 <= primer_octeto <= 223: clase = "C"
        
        if clase:
            cola_salida.put((ip, clase))

def imprimir_ips(cola_entrada):
    """Proceso 3: Imprime resultados"""
    while True:
        dato = cola_entrada.get()
        if dato is None:
            break
        print(f"IP: {dato[0]} -> Clase: {dato[1]}")

if __name__ == "__main__":
    start_time = time.time()
    
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=generar_ips, args=(q1,))
    p2 = multiprocessing.Process(target=filtrar_ips, args=(q1, q2))
    p3 = multiprocessing.Process(target=imprimir_ips, args=(q2,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    print(f"Tiempo total: {time.time() - start_time:.4f} segundos")