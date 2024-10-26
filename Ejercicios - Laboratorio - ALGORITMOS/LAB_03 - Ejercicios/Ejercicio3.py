# Inicializar una lista para almacenar las notas
notas = []

# Solicitar notas al usuario
while True:
    entrada = input("Ingrese una nota (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular el promedio si hay notas
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print("El promedio de las notas es:", promedio)
else:
    print("No se ingresaron notas.")
