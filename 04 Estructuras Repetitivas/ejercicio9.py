suma = 0

print("Ingresa 100 numeros enteros:")

for i in range(1, 101):
    num = int(input(f"{i}. Ingresa un número: "))
    suma += num 

media = suma / 100

print("La media de los números ingresados es:", media)
