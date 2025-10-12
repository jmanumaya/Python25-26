import os

if __name__ == "__main__":
    numeros_des = os.path.join(os.path.dirname(__file__), "numeros_desordenados.txt")
    numeros_ord = os.path.join(os.path.dirname(__file__), "numeros_ordenados.txt")
    numeros = []

    with open(numeros_des, "rt") as fl:
        for num in fl:
            num = num.strip()
            if num:
                numeros.append(int(num))
    
    numeros.sort()

    with open(numeros_ord, "w") as fw:
        for num in numeros:
            fw.write(f"{num}\n")
    
    print("✅ Numeros ordenados correctamente en:", numeros_ord)