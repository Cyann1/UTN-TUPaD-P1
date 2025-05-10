pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresa 100 numeros enteros:")

for i in range(1, 101):
    num = int(input(f"{i}. Ingresa un numero: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)
