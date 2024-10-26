# Solicitar el peso en kilogramos
peso = float(input("Ingrese su peso en kilogramos: "))

# Solicitar la altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar la categoría según el IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Imprimir el resultado
print(f"Su IMC es: {imc:.2f}")
print("Categoría:", categoria)
