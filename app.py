
import random

def jugar():
    elementos = ["piedra", "papel", "tijeras"]
    
    # Elección aleatoria del oponente
    oponente = random.choice(elementos)
    
    # Entrada del jugador
    jugador = input("Elige piedra, papel o tijeras: ").lower()

    # Validación de entrada del jugador
    while jugador not in elementos:
        print("Opción no válida. Inténtalo de nuevo.")
        jugador = input("Elige piedra, papel o tijeras: ").lower()

    # Determinar el resultado
    if jugador == oponente:
        print(f"Empate. Ambos eligieron {jugador}.")
        return 0
    elif (
        (jugador == "piedra" and oponente == "tijeras") or
        (jugador == "papel" and oponente == "piedra") or
        (jugador == "tijeras" and oponente == "papel")
    ):
        print(f"Ganaste. {jugador} gana a {oponente}.")
        return 1
    else:
        print(f"Perdiste. {oponente} gana a {jugador}.")
        return -1

def main():
    puntuacion = 0

    while True:
        resultado = jugar()
        puntuacion += resultado

        seguir_jugando = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if seguir_jugando != "s":
            break

    print(f"\nTu puntuación final es: {puntuacion}")

if __name__ == "__main__":
    print("¡Bienvenido al juego de piedra, papel o tijeras!\n")
    main()
