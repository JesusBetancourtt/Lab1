# Introducción a Python
Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis clara y legible, lo que facilita el aprendizaje y la escritura de código. A continuación, se presenta una breve descripción de algunos conceptos fundamentales vistos en clases Diseño de Sistemas Robóticos.

## Tipos de Variables
- **Enteros (int):** Representan números enteros, por ejemplo, `1`, `10`, `-5`.
- **Flotantes (float):** Representan números decimales, por ejemplo, `3.14`, `2.0`, `-0.5`.
- **Cadenas (str):** Representan secuencias de caracteres, por ejemplo, `"Hola"`, `'Python'`.
- **Booleanos (bool):** Representan valores de verdad, `True` o `False`.

  Ejemplos:
  ```python
  entero = 5
  decimal = 3.14
  cadena = "Hola, Python"
  booleano = True
  ```

## Estructura de un bucle `for`
El bucle `for` se utiliza para iterar sobre una secuencia (lista, tupla, cadena, etc.).

  ```python
  for variable in secuencia:
      # Cuerpo del bucle
  ```

  Ejemplo:
  ```python
  for i in range(5):
      print(i)
  ```

## Estructura de un bucle `while`
El bucle `while` se utiliza para ejecutar un bloque de código mientras una condición sea verdadera.

  ```python
  while condicion:
      # Cuerpo del bucle
  ```

  Ejemplo:
  ```python
  contador = 0
  while contador < 5:
      print(contador)
      contador += 1
  ```

## Estructura de un condicional `if`
La estructura `if` se utiliza para ejecutar un bloque de código si una condición es verdadera. Puede ir acompañada de `elif` (else if) para evaluar múltiples condiciones.

  ```python
  if condicion:
      # Cuerpo del if
  elif otra_condicion:
      # Cuerpo del elif
  else:
      # Cuerpo del else (opcional)
  ```

  Ejemplo:
  ```python
  numero = 10
  if numero > 0:
      print("Número positivo")
  elif numero < 0:
      print("Número negativo")
  else:
      print("Número es cero")
  ```

## Operadores
- **Aritméticos:** `+, -, *, /, %, **` (suma, resta, multiplicación, división, módulo, potencia).
- **Comparación:** `==, !=, <, >, <=, >=` (igual, no igual, menor, mayor, menor o igual, mayor o igual).
- **Lógicos:** `and, or, not` (y, o, no).

Estos conceptos proporcionan una base sólida para comenzar a programar en Python. 

# Problemas a resolver
## Problema 1
Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n .

```python
# Solicita al usuario que introduzca un número entero y lo guarda en la variable 'n'
n = int(input("Introduce un número entero: "))

# Calcula la suma de todos los números anteriores hasta el número ingresado por el usuario
suma = n * (n + 1) / 2

# Imprime el resultado de la suma
print("La suma de todos los numeros anteriores hasta tu numero escogido es " + str(suma))
```

Este código tiene como objetivo principal calcular la suma de todos los números naturales desde 1 hasta un número entero proporcionado por el usuario. Comienza solicitando al usuario que ingrese un número entero, luego utiliza la fórmula de la suma de una serie aritmética para calcular la suma. Finalmente, imprime el resultado junto con un mensaje informando al usuario sobre la suma de los números.

## Problema 2
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.
Después debe mostrar por pantalla la paga que le corresponde.

```Python
# Solicita al usuario que ingrese el número de horas trabajadas y lo almacena en la variable 'n'
n = int(input("Introduce el número de horas trabajadas: "))

# Solicita al usuario que ingrese el costo por hora y lo almacena en la variable 'c'
c = int(input("Introduce el costo por hora: "))

# Calcula el producto de las horas trabajadas y el costo por hora y lo almacena en la variable 'mult'
mult = n * c

# Imprime en la consola la paga correspondiente, que es el resultado de la multiplicación
print("Paga correspondida: " + str(mult))
```

Solicita al usuario que ingrese el número de horas trabajadas y el costo por hora, luego realiza el cálculo multiplicando estos dos valores. Finalmente, muestra en la consola la paga resultante.

## Problema 3
Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.
Imprime el nombre y el sueldo a pagar de cada operador

```Python
# Lista de operadores con información sobre nombre, sueldo por hora y horas trabajadas
operadores = [
    {"nombre": "Jony", "sueldo_por_hora": 10, "horas_trabajadas": 40},
    {"nombre": "André", "sueldo_por_hora": 12, "horas_trabajadas": 35},
    {"nombre": "Rocha", "sueldo_por_hora": 9, "horas_trabajadas": 45},
    {"nombre": "Joan", "sueldo_por_hora": 11, "horas_trabajadas": 38},
    {"nombre": "Aldo", "sueldo_por_hora": 10, "horas_trabajadas": 42},
    {"nombre": "Charbel", "sueldo_por_hora": 13, "horas_trabajadas": 37}
]

# Función que calcula el sueldo multiplicando el sueldo por hora y las horas trabajadas
def calcular_sueldo(nombre, sueldo_por_hora, horas_trabajadas):
    sueldo = sueldo_por_hora * horas_trabajadas
    return sueldo

# Itera sobre la lista de operadores y calcula el sueldo para cada uno
for operador in operadores:
    nombre = operador["nombre"]
    sueldo_por_hora = operador["sueldo_por_hora"]
    horas_trabajadas = operador["horas_trabajadas"]
    
    # Llama a la función calcular_sueldo para obtener el sueldo a pagar
    sueldo_a_pagar = calcular_sueldo(nombre, sueldo_por_hora, horas_trabajadas)
    
    # Imprime en la consola el sueldo que debe recibir cada operador
    print(f"El operador {nombre} debe recibir un sueldo de ${sueldo_a_pagar}.")
```

Este código gestiona la información de varios operadores, cada uno con datos como su nombre, sueldo por hora y horas trabajadas. A través de una función llamada `calcular_sueldo`, se calcula el sueldo para cada operador multiplicando el sueldo por hora y las horas trabajadas. Posteriormente, se itera sobre la lista de operadores, se utiliza la función para calcular el sueldo de cada uno, y se imprime en la consola un mensaje indicando el sueldo que debe recibir cada operador.

## Problema 4
- Crea una lista llamada numeros que contenga al menos 10 números.
- Calcula el promedio de los números pares y el producto de los números impares.
- Imprime los resultados.

```Python
# Lista de números proporcionada
numeros = [2, 7, 14, 5, 8, 11, 20, 3, 6, 9]

# Inicialización de variables para realizar cálculos
sum_pares = 0
count_pares = 0
producto_impares = 1

# Itera sobre la lista de números
for num in numeros:
    # Verifica si el número es par
    if num % 2 == 0:
        # Si es par, se suma al total de pares y se incrementa el contador
        sum_pares += num
        count_pares += 1
    else:
        # Si es impar, se multiplica al producto de impares
        producto_impares *= num

# Calcula el promedio de los números pares
promedio_pares = sum_pares / count_pares if count_pares > 0 else 0

# Imprime la lista de números, el promedio de números pares y el producto de números impares
print(f"Lista de números: {numeros}")
print(f"Promedio de números pares: {promedio_pares}")
print(f"Producto de números impares: {producto_impares}")
```

La lista, denominada numeros, contiene valores enteros y se inicializan variables como sum_pares para acumular la suma de los números pares, count_pares para contar cuántos números pares hay, y producto_impares para calcular el producto de los números impares. A través de un bucle for, el programa itera sobre cada número en la lista, verificando si es par o impar. Los números pares se suman, mientras que los impares se multiplican para obtener el producto total. Finalmente, se calcula el promedio de los números pares y se imprime la lista original de números, del promedio, y del producto de los números impares.

## Problema 5
Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generar
un número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debe
proporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle while
debe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantos
intentos el usuario logró adivinar el número.

Pista:
```Python
import random
Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
```

```Python
# Importa el módulo 'random' para generar un número aleatorio
import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializa el contador de intentos en 0
intentos = 0

# Imprime un mensaje de bienvenida al juego
print("Bienvenido al juego de adivinanzas. Adivina el número secreto entre 1 y 10.")

# Inicia un bucle while que continuará hasta que se adivine el número secreto
while True:
    try:
        # Solicita al usuario que ingrese su adivinanza y la convierte a un número entero
        guess = int(input("Ingresa tu adivinanza: "))
    except ValueError:
        # Captura la excepción si el usuario no ingresa un número válido
        print("Por favor, ingresa un número válido.")
        continue

    # Incrementa el contador de intentos en cada iteración
    intentos += 1

    # Compara la adivinanza del usuario con el número secreto
    if guess == numero_secreto:
        # Imprime un mensaje de felicitaciones si la adivinanza es correcta y termina el juego
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
        break
    elif guess < numero_secreto:
        # Indica al usuario que el número es demasiado bajo si la adivinanza es menor que el número secreto
        print("El número es demasiado bajo. ¡Intenta de nuevo!")
    else:
        # Indica al usuario que el número es demasiado alto si la adivinanza es mayor que el número secreto
        print("El número es demasiado alto. ¡Intenta de nuevo!")
```

El programa selecciona aleatoriamente un número secreto entre 1 y 10 e indica al usuario intentar adivinar el número secreto mediante un numero proporcionado. El programa verifica si la entrada es un número válido y proporciona mensajes informativos, como "demasiado bajo" o "demasiado alto", según la relación con el número secreto. El juego continúa hasta que el usuario adivina correctamente el número, momento en el cual se muestra un mensaje de felicitación junto con la cantidad de intentos realizados. El código utiliza un bucle while True para mantener el juego en curso hasta que se rompe explícitamente cuando el usuario adivina correctamente.

## Problema 6 (Robot explorador)
El programa debe generar una matriz de al menos 5x5.
El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o la
máxima posición si se cambia el tamaño de matriz.
El numero y la posición de los obstáculos es aleatoria.
El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en el
eventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”
En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres y
obstáculos de la siguiente forma X obstáculo o libre

o o o X o

o o o o o

o o o o X

o o o o o

o X X X o

Deberá imprimir también la ruta que siguió.
Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas

Pista:
- Flecha hacia arriba: ↑ (U+2191)
- Flecha hacia abajo: ↓ (U+2193)
- Flecha hacia la izquierda: ← (U+2190)
- Flecha hacia la derecha: → (U+2192



### Laberinto del Robot

El robot inicia en la esquina superior izquierda y debe llegar a la esquina inferior derecha, evitando obstáculos colocados aleatoriamente en el laberinto.

### Descripción

#### 1. Generación de Laberinto

```python
def generar_matriz(filas, columnas):
    """
    Genera una matriz cuadrada de tamaño 'filas' x 'columnas'.
    Inicializa la matriz con 'o' (espacios libres) y coloca obstáculos 'X' de manera aleatoria.
    Devuelve la matriz generada.
    """
    matriz = [['o' for _ in range(columnas)] for _ in range(filas)]
    return matriz
```

#### 2. Impresión de la Matriz

```python
def imprimir_matriz(matriz):
    """
    Imprime la matriz en la consola.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))
```

#### 3. Búsqueda del Camino

```python
def encontrar_camino(matriz, inicio, fin):
    """
    Utiliza el algoritmo de búsqueda BFS para encontrar un camino desde el 'inicio' hasta el 'fin',
    evitando obstáculos en la matriz.
    Devuelve el camino encontrado o None si no hay camino.
    """
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
```

#### 4. Impresión del Camino en la Matriz

```python
def imprimir_camino(matriz, camino):
    """
    Marca el camino en la matriz con flechas indicando la dirección de movimiento.
    Imprime la matriz con el camino en la consola.
    """
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
```

#### 5. Programa Principal

```python
def main():
    """
    Programa principal:
    - Genera el laberinto, coloca obstáculos y posiblemente en la posición inicial.
    - Busca un camino y lo imprime en la consola.
    """
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
```
