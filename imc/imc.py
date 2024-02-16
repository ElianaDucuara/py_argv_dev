# pylint: disable=W0621
from sys import argv

# Función para calcular el IMC
def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100  # Convertir altura en centímetros a metros
    imc = peso / (altura_m ** 2)  # Calcular el IMC
    return round(imc, 2)  # Redondear el IMC a dos decimales

# Función para determinar la clasificación de la OMS
def clasificacion_oms(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

# Comprobación de los argumentos necesarios
if len(argv) == 3:
    try:
        peso = float(argv[1])
        altura_cm = float(argv[2])
        imc = calcular_imc(peso, altura_cm)
        clasificacion = clasificacion_oms(imc)
        print(f"Su IMC es {imc}, La clasificación de '{clasificacion}' según la OMS.")
    except ValueError:
        print("Por favor, introduce el peso y la altura como números.")
else:
    print("Uso: python imc.py [peso en kg] [altura en cm]")
