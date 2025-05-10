num = int( input ("ingrese un numero: "))

suma = 0
for numero in range(0, num + 1):
    suma += numero

print("La suma de los numeros entre 0 y", num, "es:", suma)