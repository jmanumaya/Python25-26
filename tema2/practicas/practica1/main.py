import multiprocessing
import random
import time
import os

# Esto hace que la ruta de trabajo sea la misma donde está el archivo main.py
directorio_actual = os.path.dirname(__file__)
if directorio_actual != "":
    os.chdir(directorio_actual)

# --- FUNCIONES (Lo que hace cada proceso) ---

def generar_temperaturas(dia):
    # Paso 1: Crear el nombre del fichero ej: "01-12.txt"
    # El :02d sirve para que ponga un cero delante si es menor de 10 (01, 02...)
    nombre_fichero = f"{dia:02d}-12.txt"
    
    # Paso 2: Abrir el fichero para escribir ('w')
    with open(nombre_fichero, "w") as fichero:
        # Hacemos un bucle de 24 veces (una por hora)
        for i in range(24):
            temperatura = random.uniform(0, 20) # Número aleatorio
            temperatura = round(temperatura, 2) # Redondeamos a 2 decimales
            fichero.write(f"{temperatura}\n")   # Escribimos en el fichero

def buscar_maxima(dia):
    nombre_fichero = f"{dia:02d}-12.txt"
    
    # Solo intentamos leer si el fichero existe
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            # Leemos todas las líneas
            lineas = fichero.readlines()
            
            # Convertimos las líneas de texto a números decimales
            lista_numeros = []
            for linea in lineas:
                lista_numeros.append(float(linea.strip()))
            
            # Buscamos el máximo
            maximo = max(lista_numeros)
            
            # Escribimos el resultado en maximas.txt (modo 'a' para añadir)
            with open("maximas.txt", "a") as f_salida:
                f_salida.write(f"Dia {dia}: {maximo}\n")

def buscar_minima(dia):
    nombre_fichero = f"{dia:02d}-12.txt"
    
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, "r") as fichero:
            lineas = fichero.readlines()
            
            lista_numeros = []
            for linea in lineas:
                lista_numeros.append(float(linea.strip()))
            
            minimo = min(lista_numeros)
            
            # Escribimos el resultado en minimas.txt (modo 'a' para añadir)
            with open("minimas.txt", "a") as f_salida:
                f_salida.write(f"Dia {dia}: {minimo}\n")

# --- PROGRAMA PRINCIPAL (Main) ---

if __name__ == "__main__":
    # borramos los ficheros de resultados anteriores si existen
    if os.path.exists("maximas.txt"):
        os.remove("maximas.txt")
    if os.path.exists("minimas.txt"):
        os.remove("minimas.txt")

    print("--- FASE 1: Generando ficheros de temperatura ---")
    
    # Lista para guardar los procesos y luego poder esperarlos (join)
    lista_procesos = []

    # Bucle del día 1 al 31
    for dia in range(1, 32):
        # Creamos el proceso
        p = multiprocessing.Process(target=generar_temperaturas, args=(dia,))
        
        # Lo arrancamos
        p.start()
        
        # Lo guardamos en la lista
        lista_procesos.append(p)

    # Esperamos a que terminen todos los procesos de la Fase 1
    for p in lista_procesos:
        p.join()
    
    print("Ficheros creados correctamente.")

    print("--- FASE 2: Buscando máximas y mínimas ---")
    
    lista_procesos_lectura = []

    # Bucle del día 1 al 31 otra vez
    for dia in range(1, 32):
        # Proceso para la máxima
        p1 = multiprocessing.Process(target=buscar_maxima, args=(dia,))
        p1.start()
        lista_procesos_lectura.append(p1)

        # Proceso para la mínima
        p2 = multiprocessing.Process(target=buscar_minima, args=(dia,))
        p2.start()
        lista_procesos_lectura.append(p2)

    # Esperamos a que terminen todos los procesos de lectura
    for p in lista_procesos_lectura:
        p.join()

    print("Fin del programa.")