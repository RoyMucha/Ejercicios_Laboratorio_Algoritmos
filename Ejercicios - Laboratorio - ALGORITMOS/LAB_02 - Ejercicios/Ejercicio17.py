# Pedir al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Pedir al usuario que ingrese el prefijo y sufijo a verificar
prefijo = input("Ingresa el prefijo a verificar: ")
sufijo = input("Ingresa el sufijo a verificar: ")

# Verificar si la cadena comienza con el prefijo y termina con el sufijo
empieza_con_prefijo = cadena.startswith(prefijo)
termina_con_sufijo = cadena.endswith(sufijo)

# Imprimir los resultados
if empieza_con_prefijo:
    print("La cadena comienza con el prefijo '" + prefijo + "'.")
else:
    print("La cadena NO comienza con el prefijo '" + prefijo + "'.")

if termina_con_sufijo:
    print("La cadena termina con el sufijo '" + sufijo + "'.")
else:
    print("La cadena NO termina con el sufijo '" + sufijo + "'.")
