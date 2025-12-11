import os

if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(__file__), "pruebas.txt")

    with open(ruta, 'w', encoding="utf8") as f:
        print("Escribe líneas para guardar en el archivo (escribe 'fin' para terminar)")
        entrada = input("Introduce lo que quieras guardar: ")

        while(entrada != "fin"):
            f.write(f"{entrada}\n")
            entrada = input("Introduce lo que quieras guardar: ")
    print("✅ Archivo guardado correctamente en:", ruta)