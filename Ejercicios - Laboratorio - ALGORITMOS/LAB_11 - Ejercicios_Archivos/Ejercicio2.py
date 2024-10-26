#"Analizador de datos": Escribe un programa que lea un archivo CSV con datos (por ejemplo, temperaturas 
#diarias, precios de acciones, etc.) y calcule la media, el valor máximo y el valor mínimo de los datos.

import csv

# Solicitar el nombre del archivo CSV
nombre_archivo = input("Ingresa el nombre del archivo CSV (incluye .csv): ")

# Inicializar una lista para almacenar los datos numéricos
datos = []

# Leer el archivo CSV
try:
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        # Omitir la primera fila si contiene encabezados
        next(lector_csv)
        
        # Leer cada fila y agregar el valor numérico a la lista de datos
        for fila in lector_csv:
            # Suponemos que los datos numéricos están en la primera columna (índice 0)
            datos.append(float(fila[0]))

    # Calcular la media, el máximo y el mínimo
    media = sum(datos) / len(datos)
    valor_maximo = max(datos)
    valor_minimo = min(datos)

    # Mostrar los resultados
    print("Media de los datos:", media)
    print("Valor máximo:", valor_maximo)
    print("Valor mínimo:", valor_minimo)

except FileNotFoundError:
    print("El archivo no se encontró.")
except ValueError:
    print("Error: Asegúrate de que los datos son numéricos y están en la primera columna del archivo CSV.")
except ZeroDivisionError:
    print("Error: El archivo CSV está vacío o no contiene datos numéricos.")
