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