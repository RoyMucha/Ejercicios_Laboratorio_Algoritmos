
n = int(input("Ingresa un número entero positivo para el número de filas: "))

for i in range(1, n + 1): 
    for j in range(i):  
        print("*", end=" ")  
    print()  
