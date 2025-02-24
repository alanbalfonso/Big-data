import random

def imprimir_tablero(tablero):
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    return any(all(tablero[i] == jugador for i in combinacion) for combinacion in combinaciones_ganadoras)

def tablero_lleno(tablero):
    return all(isinstance(c, str) for c in tablero)

def obtener_movimiento_usuario(tablero):
    while True:
        try:
            movimiento = int(input("Tu turno (elige un número del 1 al 9): ")) - 1
            if 0 <= movimiento < 9 and isinstance(tablero[movimiento], int):
                return movimiento
            print("Movimiento inválido, intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, ingresa un número.")

def obtener_movimiento_maquina(tablero):
    movimientos_disponibles = [i for i in range(9) if isinstance(tablero[i], int)]
    return random.choice(movimientos_disponibles)

def main():
    tablero = [i+1 for i in range(9)]  # Tablero con números del 1 al 9
    tablero[4] = 'X'  # La máquina siempre empieza en el centro
    print("\nBienvenido al Tic-Tac-Toe!\n")
    imprimir_tablero(tablero)

    while True:
        movimiento_usuario = obtener_movimiento_usuario(tablero)
        tablero[movimiento_usuario] = 'O'
        imprimir_tablero(tablero)

        if verificar_ganador(tablero, 'O'):
            print("¡Felicidades! Has ganado.")
            break
        if tablero_lleno(tablero):
            print("El juego termina en empate.")
            break

        print("Turno de la máquina...")
        movimiento_maquina = obtener_movimiento_maquina(tablero)
        tablero[movimiento_maquina] = 'X'
        imprimir_tablero(tablero)

        if verificar_ganador(tablero, 'X'):
            print("La máquina gana. ¡Suerte la próxima vez!")
            break
        if tablero_lleno(tablero):
            print("El juego termina en empate.")
            break

if __name__ == "__main__":
    main()
