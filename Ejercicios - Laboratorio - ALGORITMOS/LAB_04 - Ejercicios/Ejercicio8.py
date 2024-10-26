n = int(input("Ingresa un número entero positivo: "))

if n == 0:
    fibonacci = 0
elif n == 1:
    fibonacci = 1
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        fibonacci = a + b
        a, b = b, fibonacci

print("El enésimo número de Fibonacci es:", fibonacci)
