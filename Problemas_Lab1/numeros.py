numeros = [2, 7, 14, 5, 8, 11, 20, 3, 6, 9]

sum_pares = 0
count_pares = 0
producto_impares = 1

for num in numeros:
    if num % 2 == 0:
        sum_pares += num
        count_pares += 1
    else:
        producto_impares *= num

promedio_pares = sum_pares / count_pares if count_pares > 0 else 0

print(f"Lista de números: {numeros}")
print(f"Promedio de números pares: {promedio_pares}")
print(f"Producto de números impares: {producto_impares}")