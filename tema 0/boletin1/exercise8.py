'''
Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
'''

# Promp the user a number
n = int(input("Please enter the base/height of the Triangle (n): "))

if n <= 0:
    print("Please enter a positive number.")
else:
    for i in range(1, n + 1):
        # Spaces in the left and then i asterisks split by a space 
        left = " " * (n - i)
        asterisks = " ".join(["*"] * i)
        print(left + asterisks)

