import os

if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(__file__), "Alumnos.txt")

    # Usando with cierra el archivo automáticamente
    with open(ruta, 'rt') as f:
        edades = 0
        estaturas = 0
        count = 0

        for linea in f:
            # strip() elimina los saltos de línea y espacios extra
            name, edad, altura = linea.strip().split()
            print(name)
            edades += int(edad)
            estaturas += float(altura)
            count += 1

    media_edad = edades / count
    media_estaturas = estaturas / count
    print(f"Media de Edades: {media_edad:.2f}, Media de Estaturas: {media_estaturas:.2f}")
