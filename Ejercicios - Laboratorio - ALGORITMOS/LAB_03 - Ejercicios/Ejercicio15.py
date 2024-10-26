# Solicitar un número de teléfono de 10 dígitos
numero_telefono = input("Ingrese un número de teléfono de 10 dígitos: ")

# Verificar que el número tenga 10 dígitos
if len(numero_telefono) == 10 and numero_telefono.isdigit():
    # Formatear el número de teléfono
    telefono_formateado = "(" + numero_telefono[:3] + ") " + numero_telefono[3:6] + "-" + numero_telefono[6:]
    print("Número de teléfono formateado:", telefono_formateado)
else:
    print("Número inválido. Asegúrese de ingresar exactamente 10 dígitos.")
