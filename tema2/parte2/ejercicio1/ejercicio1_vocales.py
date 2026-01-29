import multiprocessing
import time
import os

def contar_vocal(vocal, ruta_archivo):
    count = 0
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            texto = f.read().lower()
            count = texto.count(vocal)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
    return (vocal, count)

if __name__ == "__main__":
    start_time = time.time()
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_txt = os.path.join(carpeta_actual, "texto.txt")
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    argumentos = [(v, ruta_txt) for v in vocales]
    
    print(f"Leyendo archivo: {ruta_txt}")
    print(f"Iniciando conteo para: {vocales}")
    
    with multiprocessing.Pool(processes=5) as pool:
        resultados = pool.starmap(contar_vocal, argumentos)
        
    print("Resultados:", resultados)
    print(f"Tiempo total: {time.time() - start_time:.4f} segundos")