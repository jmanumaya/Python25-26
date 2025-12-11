from producto import Producto
from perecedero import Perecedero
from no_perecedero import No_perecedero

if __name__ == "__main__":
    productos = [
        Producto("Agua", 1.0),
        Perecedero("Leche", 2.0, 2),
        Perecedero("Yogur", 1.5, 1),
        No_perecedero("Arroz", 3.0, "Cereal"),
    ]

    print("=== LISTA DE PRODUCTOS ===")
    for p in productos:
        print(p)

    print("\n=== CÁLCULO DE PRECIOS PARA 5 UNIDADES ===")
    for p in productos:
        print(f"{p.nombre}: {p.calcular(5):.2f}€")

    print("\n=== PRODUCTOS ORDENADOS POR PRECIO ===")
    for p in sorted(productos):
        print(p)