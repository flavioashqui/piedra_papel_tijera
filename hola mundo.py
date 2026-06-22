import random

opciones = ("piedra", "papel", "tijera")

puntos_usuario = 0
puntos_computadora = 0
empates = 0

print("=====BIENVENIDOS AL JUEGO======= ")
print("     JUEGO: PIEDRA, PAPEL O TIJERA")
while True:
    usuario = input("\nElige piedra, papel o tijera: ").lower().strip()

    if usuario not in opciones:
        print("Opción inválida. Debes escribir piedra, papel o tijera.")
        continue

    computadora = random.choice(opciones)

    print("\nTu elección:", usuario)
    print("Elección de la computadora:", computadora)

    if usuario == computadora:
        print("Resultado: Empate.")
        empates += 1

    elif (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijera" and computadora == "papel")
    ):
        print("Resultado: Ganaste esta ronda.")
        puntos_usuario += 1

    else:
        print("Resultado: La computadora ganó esta ronda.")
        puntos_computadora += 1

    print("\nMarcador:")
    print("Usuario:", puntos_usuario)
    print("Computadora:", puntos_computadora)
    print("Empates:", empates)

    jugar_otra_vez = input("\n¿Deseas jugar otra ronda? sí/no: ").lower().strip()

    if jugar_otra_vez != "si" and jugar_otra_vez != "sí":
        print("\nGracias por jugar.")
        break