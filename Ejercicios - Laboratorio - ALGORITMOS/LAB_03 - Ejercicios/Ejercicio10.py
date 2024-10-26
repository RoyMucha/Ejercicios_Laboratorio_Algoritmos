# Solicitar la longitud en metros
metros = float(input("Ingrese la longitud en metros: "))

# Solicitar la unidad a la que desea convertir
unidad = input("Ingrese la unidad a la que desea convertir (pies, pulgadas, yardas): ").lower()

# Realizar la conversión
if unidad == "pies":
    longitud_convertida = metros * 3.28084  # 1 metro = 3.28084 pies
elif unidad == "pulgadas":
    longitud_convertida = metros * 39.3701  # 1 metro = 39.3701 pulgadas
elif unidad == "yardas":
    longitud_convertida = metros * 1.09361  # 1 metro = 1.09361 yardas
else:
    longitud_convertida = None

# Imprimir el resultado
if longitud_convertida is not None:
    print(f"{metros} metros son {longitud_convertida:.2f} {unidad}.")
else:
    print("Unidad no válida. Por favor, elija 'pies', 'pulgadas' o 'yardas'.")
