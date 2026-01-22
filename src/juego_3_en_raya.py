import pytest

fichas = ['o', 'x']

def generar_tablero(n, movimientos_jugadores):
    tablero = []
    for i in range(n):
        fila = ['_' for _ in range(n)]
        for j in range(n):
            for k in range(len(movimientos_jugadores)):
                movimientos_jugador = movimientos_jugadores[k]
                if i in movimientos_jugador:
                    if j in movimientos_jugador[i]:
                        fila[j] = fichas[k]
        tablero.append(fila)
    return tablero

def movimiento_valido(x, y, movimientos_otro_jugador):
    n = 3 
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if x in movimientos_otro_jugador:
        if y in movimientos_otro_jugador[x]:
            return False
    return True

def jugada_ganadora(movimientos_jugador):
    for fila in movimientos_jugador:
        if len(movimientos_jugador[fila]) == 3:
            return True
    return False

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

if __name__ == "__main__":
    n = int(input('Introduce el tamaño del tablero cuadrado: ')) # [cite: 594]
    casillas_libres = n * n # [cite: 595]
    jugador_activo = 0 # [cite: 596]
    movimientos_jugadores = [{}, {}] # [cite: 600]

    while casillas_libres > 0: # [cite: 603]
        tablero = generar_tablero(n, movimientos_jugadores) # [cite: 601]
        mostrar_tablero(tablero) # [cite: 602]

        print(f"Turno JUGADOR {jugador_activo + 1}") # [cite: 604]
        entrada = input("Introduce movimiento (fila,columna): ") # [cite: 604]

        try:
            x = int(entrada.split(',')[0]) - 1 # [cite: 606]
            y = int(entrada.split(',')[1]) - 1 # [cite: 610]

            movs_activo = movimientos_jugadores[jugador_activo] # [cite: 613]
            movs_otro = movimientos_jugadores[(jugador_activo + 1) % 2] # [cite: 614]

            if movimiento_valido(x, y, movs_otro): # [cite: 615]
                col = movs_activo.get(x, []) # [cite: 616]
                col.append(y) # [cite: 616]
                movs_activo[x] = col # [cite: 617]
                
                if jugada_ganadora(movs_activo): # [cite: 623]
                    mostrar_tablero(generar_tablero(n, movimientos_jugadores))
                    print(f"¡ENHORABUENA EL JUGADOR {jugador_activo + 1} HA GANADO!") # [cite: 624]
                    break
                
                casillas_libres -= 1 # [cite: 629]
                jugador_activo = (jugador_activo + 1) % 2 # [cite: 630]
            else:
                print("Movimiento inválido. Inténtalo de nuevo.") # [cite: 628]
        except (ValueError, IndexError):
            print("Formato incorrecto. Usa: fila,columna (ej: 1,2)")