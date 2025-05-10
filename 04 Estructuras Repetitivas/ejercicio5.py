import random

numSecreto = random.randint(0, 9)

intentos = 0
adivinanza = -1  

print("¡Adivina el numero secreto entre 0 y 9!")

while adivinanza != numSecreto:
    adivinanza = int(input("Adivina el numero: "))
    intentos += 1

# Muestra el resultado
print("¡Correcto! El numero era", numSecreto)
print("Lo lograste en", intentos, "intentos")
