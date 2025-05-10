total = 0

numero = int(input("Ingresa un número entero (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total de los números ingresados es:", total)

