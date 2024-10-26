

n = int(input("Ingresa un número entero positivo: "))

suma = 0
contador = 2 

while contador <= n:
    suma += contador  
    contador += 2    

print("La suma de todos los números pares desde 2 hasta", n, "es:", suma)
