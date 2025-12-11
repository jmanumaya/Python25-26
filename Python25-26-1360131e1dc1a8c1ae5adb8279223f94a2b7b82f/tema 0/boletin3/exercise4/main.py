from articulo import Articulo

def main():
    a1 = Articulo("Camiseta", 20, 10)
    a2 = Articulo("Pantalón", 35, 5)

    print(a1)
    print(a2)

    print("\nPrecio con IVA de la camiseta:", a1.getPVP())
    print("Precio con IVA y descuento de 3€:", a1.getPVPDescuento(3))

    print("\nVendiendo 2 camisetas...")
    if a1.vender(2):
        print("Venta realizada correctamente.")
    else:
        print("No hay suficientes unidades.")
    print(a1)

    print("\nIntentando vender 10 pantalones...")
    if a2.vender(10):
        print("Venta realizada.")
    else:
        print("No hay stock suficiente.")
    print(a2)

    print("\nComparación de artículos (por nombre):", a1 < a2)

main()
