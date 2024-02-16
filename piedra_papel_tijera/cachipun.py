from sys import argv
import random

# Definir las opciones posibles
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador
def determinar_ganador(jugador, computadora):
    """Function printing python version."""
    if jugador == computadora:
        return "Es un empate."
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "La computadora gana."


# Comprobación de jugador ingresando  un movimiento válido
if len(argv) == 2 and argv[1] in opciones:
    jugador = argv[1]
    computadora = random.choice(opciones)
    print(f"Tú jugaste: {jugador}")
    print(f"Computador jugo: {computadora}")
    print(determinar_ganador(jugador, computadora))
else:
    print(f"Argumento inválido: Debe ser {argv[0]} [piedra|papel|tijera]")
