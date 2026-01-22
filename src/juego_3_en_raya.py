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
    # 1. Comprobamos filas
    for fila in movimientos_jugador:
        if len(movimientos_jugador[fila]) == 3:
            return True

    # 2. Comprobamos columnas
    conteo_columnas = {}
    for fila in movimientos_jugador:
        for col in movimientos_jugador[fila]:
            conteo_columnas[col] = conteo_columnas.get(col, 0) + 1
            if conteo_columnas[col] == 3:
                return True

    # 3. Comprobamos diagonales (para tablero 3x3)
    diag_principal = 0
    diag_secundaria = 0
    for fila in movimientos_jugador:
        for col in movimientos_jugador[fila]:
            if fila == col:
                diag_principal += 1
            if fila + col == 2:
                diag_secundaria += 1
                
    if diag_principal == 3 or diag_secundaria == 3:
        return True

    return False

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def test_ganador_columna():
    # Fichas en (0,0), (1,0), (2,0)
    movs = {0: [0], 1: [0], 2: [0]}
    assert jugada_ganadora(movs) is True

def test_ganador_diagonal():
    # Fichas en (0,0), (1,1), (2,2)
    movs = {0: [0], 1: [1], 2: [2]}
    assert jugada_ganadora(movs) is True
    
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