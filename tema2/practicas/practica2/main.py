import multiprocessing
import os

# --- PROCESO 1: FILTRAR POR DEPARTAMENTO ---
def filtrar_departamento(departamento_buscado, cola_salida):
    """
    Lee salarios.txt con formato: Nombre;Apellido;Salario;Departamento
    """
    ruta = os.path.join(os.path.dirname(__file__), "salarios.txt")
    
    # Abrimos con encoding utf-8 para leer bien las tildes (Gómez, Pérez...)
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue 

            # 1. Separamos por PUNTO Y COMA (;)
            datos = linea.split(';')

            if len(datos) == 4:
                nombre = datos[0].strip()
                apellido = datos[1].strip()
                salario = datos[2].strip()
                dept = datos[3].strip()

                # Comparamos ignorando mayúsculas
                if dept.lower() == departamento_buscado.lower():
                    # Preparamos un paquete con: Nombre,Apellido,Salario
                    # Usamos coma para separarlos internamente
                    paquete = f"{nombre},{apellido},{salario}"
                    cola_salida.put(paquete)

    # Avisamos que hemos terminado
    cola_salida.put(None)

# --- PROCESO 2: FILTRAR POR SALARIO ---
def filtrar_salario(salario_minimo, cola_entrada, cola_salida):
    """
    Recibe: Nombre,Apellido,Salario
    Filtra si Salario >= salario_minimo
    """
    while True:
        dato = cola_entrada.get()
        
        if dato is None:
            cola_salida.put(None) # Avisamos al siguiente
            break
        
        # Desempaquetamos lo que nos mandó el Proceso 1
        nombre, apellido, salario_str = dato.split(',')
        
        try:
            salario = float(salario_str)
            if salario >= salario_minimo:
                # Enviamos la línea tal cual llegó
                cola_salida.put(dato)
        except ValueError:
            continue

# --- PROCESO 3: ESCRIBIR ---
def escribir_empleados(cola_entrada):
    """
    Recibe: Nombre,Apellido,Salario
    Escribe: Apellido Nombre, Salario
    """
    ruta = "empleados.txt"
    # Borramos contenido anterior si existe
    if os.path.exists(ruta):
        os.remove(ruta)

    with open(ruta, "a", encoding="utf-8") as f:
        while True:
            dato = cola_entrada.get()
            
            if dato is None:
                break
            
            nombre, apellido, salario = dato.split(',')
            
            f.write(f"{apellido} {nombre}, {salario}\n")

# --- MAIN ---
if __name__ == "__main__":
    # Asegurar que estamos en la carpeta correcta
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("--- BUSCADOR DE EMPLEADOS ---")
    print("Departamentos disponibles en el archivo: Recursos Humanos, Desarrollo, Finanzas")
    
    # Inputs
    dept = input("Introduce Departamento: ")
    salario_min = float(input("Introduce Salario Mínimo: "))

    # Colas
    cola1 = multiprocessing.Queue()
    cola2 = multiprocessing.Queue()

    # Procesos
    p1 = multiprocessing.Process(target=filtrar_departamento, args=(dept, cola1))
    p2 = multiprocessing.Process(target=filtrar_salario, args=(salario_min, cola1, cola2))
    p3 = multiprocessing.Process(target=escribir_empleados, args=(cola2,))

    # Ejecución
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("\nProceso terminado. Abre 'empleados.txt' para ver el resultado.")