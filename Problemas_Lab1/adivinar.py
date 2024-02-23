import random
numero_secreto = random.randint(1, 10)
intentos = 0

print("Bienvenido al juego de adivinanzas. Adivina el número secreto entre 1 y 10.")

while True:
    try:
        guess = int(input("Ingresa tu adivinanza: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    intentos += 1

    if guess == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
        break
    elif guess < numero_secreto:
        print("El número es demasiado bajo. ¡Intenta de nuevo!")
    else:
        print("El número es demasiado alto. ¡Intenta de nuevo!")