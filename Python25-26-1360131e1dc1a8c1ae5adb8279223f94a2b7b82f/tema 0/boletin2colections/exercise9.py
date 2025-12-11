# Crea un diccionario donde las claves son las letras del abecedario y los valores, 
# la puntuación para cada letra, como en el Scrabble. El programa le pedirá una palabra al 
# usuario y se mostrará por pantalla la puntuación que tiene la palabra en total.

abecedary = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
    "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "C": 3, "M": 3, "B": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "Y": 4,
    "Q": 5,
    "J": 8, "Ñ": 8, "X": 8,
    "K": 10, "Z": 10
}

word = input("Please enter a word: ")

score = 0

for letter in word.upper():
    if letter in abecedary:
        score += abecedary[letter]

print("The score of the word is:", score)
