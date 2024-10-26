
frase = input("Ingresa una frase: ")
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in frase:
    if letra in vocales:  
        contador_vocales += 1  

print("El número total de vocales en la frase es:", contador_vocales)
