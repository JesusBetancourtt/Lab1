# Solicita al usuario que ingrese el número de horas trabajadas y lo almacena en la variable 'n'
n = int(input("Introduce el número de horas trabajadas: "))

# Solicita al usuario que ingrese el costo por hora y lo almacena en la variable 'c'
c = int(input("Introduce el costo por hora: "))

# Calcula el producto de las horas trabajadas y el costo por hora y lo almacena en la variable 'mult'
mult = n * c

# Imprime la paga correspondiente
print("Paga correspondida: " + str(mult))