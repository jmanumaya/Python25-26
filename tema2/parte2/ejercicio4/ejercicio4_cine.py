import multiprocessing
import time
import os

def filtrar_por_ano(conn, ruta_fichero, ano_buscado):
    """Proceso 1: Envía películas por Pipe (Imagen 3)"""
    print(f"Leyendo desde: {ruta_fichero}")
    try:
        with open(ruta_fichero, "r", encoding='utf-8') as f:
            for linea in f:
                if ";" in linea:
                    partes = linea.strip().split(";")
                    if len(partes) == 2:
                        titulo, ano = partes
                        if ano.strip() == str(ano_buscado):
                            conn.send(linea.strip())
        conn.send("FIN")
        conn.close()
    except FileNotFoundError:
        print("Error: Fichero de películas no encontrado.")
        conn.send("FIN")
        conn.close()

def guardar_peliculas(conn, ruta_salida):
    """Proceso 2: Recibe por Pipe y guarda"""
    with open(ruta_salida, "w", encoding='utf-8') as f:
        while True:
            datos = conn.recv()
            if datos == "FIN":
                break
            f.write(datos + "\n")
            print(f"Película guardada: {datos}")
    conn.close()

if __name__ == "__main__":
    print("--- Filtro de Películas ---")
    ano = input("Introduce un año (ej. 1999): ")
    nombre_entrada = input("Nombre fichero entrada (ej. peliculas.txt): ")
    
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_entrada = os.path.join(carpeta, nombre_entrada)
    ruta_salida = os.path.join(carpeta, f"peliculas{ano}.txt")
    
    start_time = time.time()
    
    parent_conn, child_conn = multiprocessing.Pipe()
    
    p1 = multiprocessing.Process(target=filtrar_por_ano, args=(parent_conn, ruta_entrada, ano))
    p2 = multiprocessing.Process(target=guardar_peliculas, args=(child_conn, ruta_salida))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Fichero generado en: {ruta_salida}")
    print(f"Tiempo total: {time.time() - start_time:.4f} segundos")