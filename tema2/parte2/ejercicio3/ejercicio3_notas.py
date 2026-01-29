import multiprocessing
import random
import time
import os

def generar_notas(ruta_fichero):
    """Proceso 1: Genera notas y guarda en ruta específica"""
    with open(ruta_fichero, "w") as f:
        for _ in range(6):
            nota = random.uniform(1, 10)
            f.write(f"{nota:.2f}\n")

def calcular_media(ruta_lectura, nombre_alumno, ruta_salida, lock):
    """Proceso 2: Lee, calcula media y escribe en fichero compartido"""
    try:
        with open(ruta_lectura, "r") as f:
            notas = [float(linea.strip()) for linea in f]
        
        media = sum(notas) / len(notas)
        
        with lock:
            with open(ruta_salida, "a") as f_medias:
                f_medias.write(f"{media:.2f} {nombre_alumno}\n")
    except FileNotFoundError:
        print(f"Error leyendo {ruta_lectura}")

def buscar_maxima(ruta_medias):
    """Proceso 3: Busca la nota máxima"""
    max_nota = -1.0
    mejor_alumno = ""
    try:
        with open(ruta_medias, "r") as f:
            for linea in f:
                partes = linea.split()
                if len(partes) >= 2:
                    nota = float(partes[0])
                    alumno = partes[1]
                    if nota > max_nota:
                        max_nota = nota
                        mejor_alumno = alumno
        print(f"NOTA MÁXIMA: {max_nota:.2f} obtenida por {mejor_alumno}")
    except FileNotFoundError:
        print("No se encontró el archivo de medias.")

if __name__ == "__main__":
    start_time = time.time()
    
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_medias = os.path.join(carpeta, "medias.txt")
    
    open(ruta_medias, "w").close()
    
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    
    rutas_alumnos = [os.path.join(carpeta, f"Alumno{i}.txt") for i in range(1, 11)]
    
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(generar_notas, rutas_alumnos)
    
    args_p2 = []
    for i in range(1, 11):
        ruta_lec = os.path.join(carpeta, f"Alumno{i}.txt")
        args_p2.append((ruta_lec, f"Alumno{i}", ruta_medias, lock))
    
    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(calcular_media, args_p2)

    p3 = multiprocessing.Process(target=buscar_maxima, args=(ruta_medias,))
    p3.start()
    p3.join()
    
    print(f"Tiempo total: {time.time() - start_time:.4f} segundos")