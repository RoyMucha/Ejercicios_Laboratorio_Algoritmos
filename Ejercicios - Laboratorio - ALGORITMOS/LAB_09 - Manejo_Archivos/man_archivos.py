

# #EJERCICIO_9


import os

# 5.1. Eliminar un archivo específico

# Nombre del archivo que queremos eliminar
archivo_a_eliminar = 'data3.txt'

# Crear el archivo para eliminarlo (solo para demostración)
# with open(archivo_a_eliminar, 'w') as archivo:
#     archivo.write("Este archivo será eliminado.")

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

