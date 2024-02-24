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
