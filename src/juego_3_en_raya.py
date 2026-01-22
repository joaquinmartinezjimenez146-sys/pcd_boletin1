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
    n = 3 # Definimos el tamaño del tablero localmente para la validación
    if x >= n or y >= n: # Usamos >= porque en programación se cuenta desde 0
        return False
    if x in movimientos_otro_jugador:
        movimientos_en_columna = movimientos_otro_jugador[x]
        if y in movimientos_en_columna:
            return False
    return True

# --- SECCIÓN DE TESTS ---

def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores = [mov_jugador_1, mov_jugador_2]
    n = 3
    t = generar_tablero(n, movimientos_jugadores)
    assert len(t) == n
    for fila in t:
        assert len(fila) == n

def test_movimiento_fuera_tablero():
    movimientos_otro_jugador = {}
    # Si el tablero es de 3x3, las posiciones son 0, 1, 2. La 4 está fuera.
    assert False == movimiento_valido(4, 4, movimientos_otro_jugador)

def test_movimiento_incorrecto():
    # El otro jugador ya ocupa la fila 2, columna 1
    movimientos_otro_jugador = {2: [1]}
    assert False == movimiento_valido(2, 1, movimientos_otro_jugador)

def jugada_ganadora(movimientos_jugador):
    # Comprobamos si hay 3 fichas en una misma fila
    for fila in movimientos_jugador:
        movimientos_columna = movimientos_jugador[fila]
        if len(movimientos_columna) == 3:
            return True
    return False

def test_no_ganador():
    movimientos_jugador = {2: [2, 3]}
    assert False == jugada_ganadora(movimientos_jugador)

def test_ganador():
    movimientos_jugador = {2: [1, 2, 3]}
    assert True == jugada_ganadora(movimientos_jugador)