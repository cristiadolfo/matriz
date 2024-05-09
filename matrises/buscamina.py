import random

def crear_tablero(filas, columnas, minas):
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    for _ in range(minas):
        fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        while tablero[fila][columna] == -1:
            fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        tablero[fila][columna] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= fila + i < filas and 0 <= columna + j < columnas and tablero[fila + i][columna + j] != -1:
                    tablero[fila + i][columna + j] += 1
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == -1:
                print('*', end=' ')
            else:
                print(elemento, end=' ')
        print()

def jugar():
    filas, columnas, minas = 5, 5, 5
    tablero = crear_tablero(filas, columnas, minas)
    tablero_visible = [['-' for _ in range(columnas)] for _ in range(filas)]
    minas_restantes = minas

    while minas_restantes > 0:
        print("Tablero Actual:")
        mostrar_tablero(tablero_visible)
        fila = int(input("Ingrese fila (0-4): "))
        columna = int(input("Ingrese columna (0-4): "))

        if tablero[fila][columna] == -1:
            print("¡Has perdido! Una mina explotó.")
            print("Tablero Final:")
            mostrar_tablero(tablero)
            break
        else:
            tablero_visible[fila][columna] = str(tablero[fila][columna])
            minas_restantes -= 1
            if minas_restantes == 0:
                print("¡Has ganado! Has encontrado todas las minas.")
                print("Tablero Final:")
                mostrar_tablero(tablero)

jugar()