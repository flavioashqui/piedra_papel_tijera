import random

opciones = ("piedra", "papel", "tijera")

puntos_usuario = 0
puntos_computadora = 0
empates = 0


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Jugar")
    print("2. Ver marcador")
    print("3. Salir")


def jugar():
    global puntos_usuario, puntos_computadora, empates

    usuario = input("\nElige piedra, papel o tijera: ").lower().strip()

    if usuario not in opciones:
        print("Opción inválida. Debes escribir piedra, papel o tijera.")
        return

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


def mostrar_marcador():
    print("\n===== MARCADOR =====")
    print("Usuario:", puntos_usuario)
    print("Computadora:", puntos_computadora)
    print("Empates:", empates)


def guardar_estadisticas():
    archivo = open("estadisticas_juego.txt", "w", encoding="utf-8")

    archivo.write("===== ESTADÍSTICAS DEL JUEGO =====\n")
    archivo.write("Juego: Piedra, Papel o Tijera\n\n")
    archivo.write("Puntos del usuario: " + str(puntos_usuario) + "\n")
    archivo.write("Puntos de la computadora: " + str(puntos_computadora) + "\n")
    archivo.write("Empates: " + str(empates) + "\n")

    archivo.close()


print("===== BIENVENIDOS AL JUEGO =====")
print("     JUEGO: PIEDRA, PAPEL O TIJERA")

while True:
    mostrar_menu()

    opcion_menu = input("Selecciona una opción: ").strip()

    if opcion_menu == "1":
        jugar()
        mostrar_marcador()

    elif opcion_menu == "2":
        mostrar_marcador()

    elif opcion_menu == "3":
        guardar_estadisticas()
        print("\nGracias por jugar.")
        print("Resultado final:")
        mostrar_marcador()
        print("Las estadísticas fueron guardadas en el archivo estadisticas_juego.txt")
        break

    else:
        print("Opción inválida. Debes seleccionar 1, 2 o 3.")