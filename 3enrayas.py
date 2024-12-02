import random
import os
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def inicializar_juego():
    """Función que inicializa los valores del juego"""
    print("\033[0;31m ¡Bienvenidos al Tres en Raya!\033[0m")
    jugadores = [
        [input(Fore.YELLOW + "Jugador 1 (X), introduce tu nombre: "), "X"],
        [input(Fore.GREEN + "Jugador 2 (O), introduce tu nombre: "), "O"]
    ]
    jugador_actual = random.randint(0, 1)
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    return True, jugadores, jugador_actual, tablero

def dibujar_tablero(tablero):
    """Dibuja el tablero con colores"""
    print(Fore.CYAN + "   1   2   3")
    for i, fila in enumerate(tablero, start=1):
        print(Fore.CYAN + f"{i} " + " | ".join(
            [Fore.YELLOW + celda if celda == "X" else Fore.GREEN + celda if celda == "O" else Fore.WHITE + celda
             for celda in fila]
        ))
        if i < 3:
            print(Fore.CYAN + "  ---+---+---")

def entrada_valida(tablero_actual):
    """Pide coordenadas válidas al usuario"""
    while True:
        try:
            entrada = input(Fore.WHITE + "Elige coordenadas (fila columna): ")
            fila, columna = map(int, entrada.split())
            if 1 <= fila <= 3 and 1 <= columna <= 3 and tablero_actual[fila - 1][columna - 1] == "-":
                return fila, columna
            print(Fore.RED + "Coordenadas inválidas o casilla ya ocupada. Intenta de nuevo.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingresa dos números separados por un espacio.")

def actualizar_tablero(jugador, fila, columna, tablero):
    """Actualiza el tablero con la acción del jugador actual"""
    tablero[fila - 1][columna - 1] = jugador[1]
    return tablero

def tablero_completo(tablero):
    """Comprueba si el tablero está completo"""
    return all(celda != "-" for fila in tablero for celda in fila)

def comprobar_ganador(jugador, tablero):
    """Comprueba si el jugador actual ha ganado"""
    simbolo = jugador[1]
    # Filas, columnas y diagonales
    return any(
        all(tablero[i][j] == simbolo for j in range(3)) or  # Filas
        all(tablero[j][i] == simbolo for j in range(3)) or  # Columnas
        all(tablero[j][j] == simbolo for j in range(3)) or  # Diagonal principal
        all(tablero[j][2 - j] == simbolo for j in range(3))  # Diagonal secundaria
        for i in range(3)
    )

def limpiar_pantalla():
    """Limpia la consola"""
    os.system("cls" if os.name == "nt" else "clear")

# Inicio del juego
juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()

while juego_en_curso:
    limpiar_pantalla()
    print(Fore.CYAN + f"Turno de: {jugadores[jugador_actual][0]} ({jugadores[jugador_actual][1]})")
    dibujar_tablero(tablero)

    # Pedir coordenadas
    fila, columna = entrada_valida(tablero)

    # Actualizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], fila, columna, tablero)

    # Comprobar ganador
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        limpiar_pantalla()
        dibujar_tablero(tablero)
        print(Fore.GREEN + f"¡Felicidades, {jugadores[jugador_actual][0]}! Has ganado.")
        juego_en_curso = False
        break

    # Comprobar si el tablero está lleno
    if tablero_completo(tablero):
        limpiar_pantalla()
        dibujar_tablero(tablero)
        print(Fore.YELLOW + "El juego ha terminado en empate.")
        juego_en_curso = False
        break

    # Cambiar de jugador
    jugador_actual = 1 - jugador_actual

print(Fore.CYAN + "¡Gracias por jugar al Tres en Raya!")
