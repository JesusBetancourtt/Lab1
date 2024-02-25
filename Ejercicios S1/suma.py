# Solicita al usuario que introduzca un número entero y lo guarda en la variable 'n'
n = int(input("Introduce un número entero: "))

# Calcula la suma de todos los números anteriores hasta el número ingresado por el usuario
suma = n * (n + 1) / 2

# Imprime el resultado de la suma
print("La suma de todos los numeros anteriores hasta tu numero escogido es " + str(suma))