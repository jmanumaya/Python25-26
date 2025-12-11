from punto import Punto

def main():

    punto1 = Punto(3, 4)
    punto2 = Punto(3, 4)

    print(punto1)
    print(punto2)

    punto1.setXY(5, 4)

    punto2.desplaza(1,1)

    print(punto1)
    print(punto2)

    distancia = punto2.distancia(punto1)

    print(distancia)

main()