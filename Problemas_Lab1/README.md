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
en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enteros
positivos puede ser calculada de la siguiente forma:

## Problema 2
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.
Después debe mostrar por pantalla la paga que le corresponde.

## Problema 3
Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.
Imprime el nombre y el sueldo a pagar de cada operador

## Problema 4
- • Crea una lista llamada numeros que contenga al menos 10 números.
- • Calcula el promedio de los números pares y el producto de los números impares.
- • Imprime los resultados.

## Problema 5
Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generar
un número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debe
proporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle while
debe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantos
intentos el usuario logró adivinar el número.
- Pista:
```Python
import random
Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
```


## Problema 6(Robot explorador)
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

- o o o o X
- o o o o o
- o X X X o
Deberá imprimir también la ruta que siguió.
- Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas
- Pista:
- Flecha hacia arriba: ↑ (U+2191)
- Flecha hacia abajo: ↓ (U+2193)
- Flecha hacia la izquierda: ← (U+2190)
- Flecha hacia la derecha: → (U+2192
