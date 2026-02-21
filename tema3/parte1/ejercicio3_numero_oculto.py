import threading
import random

class Adivinador(threading.Thread):
    numero_oculto = random.randint(0, 100)
    alguien_acerto = False

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while not Adivinador.alguien_acerto:
            intento = random.randint(0, 100)
            if intento == Adivinador.numero_oculto:
                Adivinador.alguien_acerto = True
                print(f"{self.name} ha acertado el numero {intento}")
                return
            else:
                if Adivinador.alguien_acerto:
                    return
                print(f"{self.name} prueba con {intento}, no es correcto")

if __name__ == "__main__":
    print(f"Numero oculto: {Adivinador.numero_oculto}")
    hilos = [Adivinador(f"Hilo-{i}") for i in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
