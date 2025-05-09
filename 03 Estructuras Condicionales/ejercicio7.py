frase = str(input("Ingrese una frase o palabra: "))

vocal = "a", "e", "i", "o", "u"
exclamacion = "!"

if frase[-1] in vocal:
    frase += exclamacion

print(frase)


