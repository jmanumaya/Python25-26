# Pedir dos números y mostrarlos ordenados de menor a mayor.

# Prompt the user for two numbers.
number_one = int(input("Please enter a number: "))
number_two = int(input("Please enter another number: "))

# Use a ternary operator to sort and format the output string.
result = (f"{number_two}, {number_one}") if number_one > number_two else (f"{number_one}, {number_two}")
print(result)