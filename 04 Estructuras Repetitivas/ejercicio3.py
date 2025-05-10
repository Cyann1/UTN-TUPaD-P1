num1 = int( input ("Ingrese un numero entero: "))
num2 = int( input ("ingrese otro numero: "))

limiteMax = max(num1, num2) 
limiteMin = min(num1, num2) + 1

suma = 0
for numero in range(limiteMin, limiteMax):
    suma += numero

print("La suma de los números entre", num1, "y", num2, "es:", suma)