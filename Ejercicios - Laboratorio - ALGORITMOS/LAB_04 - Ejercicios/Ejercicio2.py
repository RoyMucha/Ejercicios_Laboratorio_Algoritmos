
numero = int(input("Ingresa un número entero positivo: "))

print("Secuencia de Collatz:")

while numero != 1:
    print(numero)  
    if numero % 2 == 0:  
        numero = numero // 2  
    else: 
        numero = 3 * numero + 1  

print(1)
