# Lista de edades
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordenar la lista y encontrar la edad mínima y máxima
edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]

# b. Añadir de nuevo la edad mínima y máxima a la lista
edades.append(edad_minima)
edades.append(edad_maxima)

# c. Encontrar la edad mediana
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2
else:
    mediana = edades[n//2]

# d. Encontrar la edad promedio
promedio = sum(edades) / len(edades)

# e. Encontrar el rango de las edades
rango = edad_maxima - edad_minima

# f. Comparar (mínimo - promedio) y (máximo - promedio) usando abs()
diferencia_minimo_promedio = abs(edad_minima - promedio)
diferencia_maximo_promedio = abs(edad_maxima - promedio)

# Imprimir resultados
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Edad mediana:", mediana)
print("Edad promedio:", promedio)
print("Rango de edades:", rango)
print("Diferencia mínima - promedio:", diferencia_minimo_promedio)
print("Diferencia máxima - promedio:", diferencia_maximo_promedio)
