numero = int(input("Ingresa un número entero positivo: "))
suma_digitos = 0

while numero > 0:
    digito = numero % 10
    suma_digitos += digito
    numero //= 10

print("La suma de los dígitos es:", suma_digitos)
