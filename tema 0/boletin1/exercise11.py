# Crear una función que devuelva un tipo booleano que indique si el carácter que se 
# pasa como parámetro de entrada corresponde con una vocal.

# Function to check if letter is a vocal
def check_vocal(letter):
    res = False
    if letter.lower() in "aeiou":
        res = True
    return res

# Method main where promp the user a letter and call the check_vocal function to check if his is a vocal
def main():
    letter = input("Please enter a letter: ")

    while len(letter) > 1:
        letter = input("Please enter a letter: ")

    print(f"{letter} is a vocal") if check_vocal(letter) else print(f"{letter} not is a vocal")

# A start call of main
main()