import os

if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(__file__), "datos.txt")

    nombre = input("Introduce tu nombre: ").strip()
    edad = int(input("Introduce tu edad: "))

    with open(ruta, 'a', encoding="utf8") as f:
        f.write(f"{nombre} {edad}\n")

    print("✅ Archivo guardado correctamente en:", ruta)