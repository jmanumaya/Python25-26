import threading
import time
import os

class ContadorVocal(threading.Thread):
    def __init__(self, vocal, ruta_archivo):
        threading.Thread.__init__(self, name=f"Hilo-{vocal}")
        self.vocal = vocal
        self.ruta_archivo = ruta_archivo
        self.resultado = (vocal, 0)

    def run(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
                texto = f.read().lower()
                count = texto.count(self.vocal)
                self.resultado = (self.vocal, count)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta_archivo}")

if __name__ == "__main__":
    start_time = time.time()

    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_txt = os.path.join(carpeta_actual, "texto.txt")

    vocales = ['a', 'e', 'i', 'o', 'u']

    print(f"Leyendo archivo: {ruta_txt}")
    print(f"Iniciando conteo para: {vocales}")

    hilos = [ContadorVocal(vocal, ruta_txt) for vocal in vocales]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    resultados = [hilo.resultado for hilo in hilos]
    print("Resultados:", resultados)
    print(f"Tiempo total: {time.time() - start_time:.4f} segundos")