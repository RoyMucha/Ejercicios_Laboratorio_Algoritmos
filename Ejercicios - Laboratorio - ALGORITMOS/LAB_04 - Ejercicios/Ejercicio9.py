cadena = input("Ingresa una cadena: ")
palindromo = True

longitud = len(cadena)

for i in range(longitud // 2):
    if cadena[i] != cadena[longitud - 1 - i]:
        palindromo = False
        break

if palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")
