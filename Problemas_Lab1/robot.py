import random

def generar_matriz(filas, columnas):
    matriz = [['o' for _ in range(columnas)] for _ in range(filas)]
    return matriz

def generar_obstaculos(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    cantidad_obstaculos = random.randint(1, filas * columnas // 2)

    for _ in range(cantidad_obstaculos):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        matriz[fila][columna] = 'X'

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def encontrar_camino(matriz, inicio, fin):
    if inicio == fin:
        return [inicio]

    filas = len(matriz)
    columnas = len(matriz[0])

    visitado = set()
    queue = [(inicio, [])]

    while queue:
        actual, ruta = queue.pop(0)

        if actual == fin:
            return ruta + [actual]

        if actual in visitado:
            continue

        visitado.add(actual)
        fila, columna = actual

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        movimientos = [(fila - 1, columna), (fila + 1, columna), (fila, columna - 1), (fila, columna + 1)]

        for movimiento in movimientos:
            nueva_fila, nueva_columna = movimiento

            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and matriz[nueva_fila][nueva_columna] != 'X':
                queue.append(((nueva_fila, nueva_columna), ruta + [actual]))

    return None

def imprimir_camino(matriz, camino):
    for i in range(len(camino) - 1):
        fila_actual, columna_actual = camino[i]
        fila_siguiente, columna_siguiente = camino[i + 1]

        if fila_siguiente > fila_actual:
            matriz[fila_actual][columna_actual] = '↓'
        elif fila_siguiente < fila_actual:
            matriz[fila_actual][columna_actual] = '↑'
        elif columna_siguiente > columna_actual:
            matriz[fila_actual][columna_actual] = '→'
        elif columna_siguiente < columna_actual:
            matriz[fila_actual][columna_actual] = '←'

    # Indicar la dirección en la posición final
    fila_final, columna_final = camino[-1]
    matriz[fila_final][columna_final] = '↓' if fila_final < len(matriz)-1 else '↑' if fila_final > 0 else '←' if columna_final > 0 else '→'

    imprimir_matriz(matriz)

def main():
    filas = 5
    columnas = 5

    matriz = generar_matriz(filas, columnas)
    matriz = generar_obstaculos(matriz)

    # Considerar la posibilidad de obstáculo en la posición inicial
    if random.choice([True, False]):
        matriz[0][0] = 'X'

    inicio = (0, 0)
    fin = (filas - 1, columnas - 1)

    if matriz[inicio[0]][inicio[1]] == 'X' or matriz[fin[0]][fin[1]] == 'X':
        print("Imposible llegar al destino")
        imprimir_matriz(matriz)
        return

    camino = encontrar_camino(matriz, inicio, fin)

    print("Mapa:")
    imprimir_matriz(matriz)

    if camino:
        print("\nMapa con camino:")
        imprimir_camino(matriz, camino)
        print("\nRuta seguida por el robot:")
        print(camino)
    else:
        print("\nImposible llegar al destino")

if __name__ == "__main__":
    main()