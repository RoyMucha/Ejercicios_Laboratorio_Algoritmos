def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convertir_temperatura():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        unidad = input("Ingrese la unidad (C para Celsius, F para Fahrenheit): ").strip().upper()

        if unidad == 'C':
            resultado = celsius_a_fahrenheit(temperatura)
            print("{:.2f} °C es igual a {:.2f} °F".format(temperatura, resultado))
        elif unidad == 'F':
            resultado = fahrenheit_a_celsius(temperatura)
            print("{:.2f} °F es igual a {:.2f} °C".format(temperatura, resultado))
        else:
            print("Unidad no válida. Por favor, use 'C' para Celsius o 'F' para Fahrenheit.")
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número para la temperatura.")

# Llamar a la función para realizar la conversión
convertir_temperatura()
