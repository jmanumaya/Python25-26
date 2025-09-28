# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

# Promp the user a number
number = int(input("Please enter a number: "))

# Function to know if the number is prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # from 2 to square of number
        if n % i == 0:
            return False
    return True

# Show Results
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")