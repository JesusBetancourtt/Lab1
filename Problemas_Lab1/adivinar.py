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