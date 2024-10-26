
#Ejercicio1

archivo = open('data2.txt', 'r')
contenido = archivo.read()  # Leer todo el contenido
print("Contenido de 'data2.txt':\n", contenido)
archivo.close()  # Importante cerrar el archivo para liberar recursos


#EJERCICIO2.

# Abrir 'data2.txt' usando with (se cierra automáticamente al finalizar)

with open('data2.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido leído con 'with open()' de 'data2.txt':\n", contenido)


#EJERCICIO3

with open('data2.txt', 'r') as archivo:
    contenido_completo = archivo.read()
    print("\nContenido completo con read():\n", contenido_completo)


#EJERCICIO4

with open('data2.txt', 'r') as archivo:
    print("\nLeyendo línea por línea con readline():")
    linea = archivo.readline()
    while linea:
        print(linea, end='')  # end evita agregar una nueva línea extra
        linea = archivo.readline()


#EJERCICIO5

with open('data2.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print("\n\nLíneas leídas con readlines():")
    print(lineas)


#EJERCICIO6

import csv

# Leer el archivo CSV y procesarlo
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    print("\nContenido de 'datos.csv':")
    for fila in lector_csv:
        print(fila)


#EJERCICIO_7

with open('nuevo_archivo.txt', 'w') as archivo_nuevo:
    archivo_nuevo.write("Lenguajes de Programación\n")
    archivo_nuevo.write("==========================\n")
    archivo_nuevo.write("Los lenguajes de programación son herramientas fundamentales en el desarrollo de software. A continuación se listan algunos de los lenguajes más populares:\n\n")

# #EJERCICIO_8

lineas = [
    "1. Python:\n",
    "   - Popular por su sintaxis sencilla y versatilidad.\n",
    "   - Muy utilizado en ciencia de datos, inteligencia artificial y desarrollo web.\n\n",
    "2. JavaScript:\n",
    "   - Lenguaje principal para desarrollo web en el lado del cliente.\n",
    "   - Compatible con frameworks como React y Node.js para desarrollo full-stack.\n\n",
    "3. Java:\n",
    "   - Usado en aplicaciones empresariales y desarrollo de Android.\n",
    "   - Es conocido por su filosofía 'escribe una vez, ejecuta en cualquier lugar'.\n\n",
    "4. C++:\n",
    "   - Un lenguaje de alto rendimiento usado en sistemas embebidos y videojuegos.\n",
    "   - Proporciona control detallado sobre la memoria del sistema.\n\n",
]
with open('nuevo_archivo.txt', 'a') as archivo_nuevo:
    archivo_nuevo.writelines(lineas)    

# #EJERCICIO_9


import os

# 5.1. Eliminar un archivo específico

# Nombre del archivo que queremos eliminar
archivo_a_eliminar = 'data1.txt'

# Crear el archivo para eliminarlo (solo para demostración)
with open(archivo_a_eliminar, 'w') as archivo:
    archivo.write("Este archivo será eliminado.")

# 5.2. Verificar si el archivo existe antes de eliminarlo


# Ejercicio 10

# Usamos try-except para manejar posibles errores si el archivo no existe
try:
    # Verificar si el archivo existe antes de eliminar
    if os.path.exists(archivo_a_eliminar):
        os.remove(archivo_a_eliminar)  # Eliminar el archivo
        print("Archivo '" + archivo_a_eliminar + "' eliminado con éxito.")
    else:
        print("El archivo '" + archivo_a_eliminar + "' no existe.")
except Exception as e:
    # Capturar cualquier otro error que pueda ocurrir
    print("Ocurrió un error al intentar eliminar el archivo: " + str(e))