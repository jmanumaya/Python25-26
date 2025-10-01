# Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
# El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada vez que encuentre 
# en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.

diccionary = {
    "e": "p",
    "i": "v",
    "k": "i",
    "m": "u",
    "p": "m",
    "q": "t",
    "r": "e",
    "s": "r",
    "t": "k",
    "u": "q",
    "v": "s",
    " ": " "
}

phrase = input("Please enter a word to encript: ").lower()
new_phrase = ""

for letter in phrase:
    if letter in diccionary:
        new_phrase += diccionary[letter]
    else:
        new_phrase += letter

print(new_phrase)