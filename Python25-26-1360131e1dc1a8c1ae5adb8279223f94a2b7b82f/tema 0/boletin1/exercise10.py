# Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.

# Function to know the max number of a range
def know_max(num1, num2): return max(num1, num2)

# Method main to promp the user two numbers and call the know_max function to know the max number
def main():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("And now, enter another number: "))

    max = know_max(num1, num2)

    print(f"Max number: {max}")

# A start call of main
main()