# Solicitar al usuario que introduzca el número de años vividos
anos = int(input("Introduce el número de años que has vivido: "))

# Calcular el número de segundos vividos
segundos_por_ano = 31536000  # 60 segundos * 60 minutos * 24 horas * 365 días
segundos_vividos = anos * segundos_por_ano

# Mostrar el resultado
print("Has vivido durante", segundos_vividos, "segundos.")
