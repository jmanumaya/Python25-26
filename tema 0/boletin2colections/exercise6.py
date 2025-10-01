# Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.

text = input("Please whrite a text: ")

text = text.lower()

words = text.split()
frecuency = {}
print(words)

for word in words:
    if word in frecuency:
        frecuency[word] += 1
    else:
        frecuency[word] = 1

print(frecuency)

