nombre = input ("Ingrese su nombre: ")


print("1. Si quiere su nombre en mayusculas")
print("2. Si quiere su nombre en minusculas")
print("3. si quiere su nombre con la primer letra mayuscula")

opcion = input("Ahora elija una opcion (1, 2 o 3): ")

if opcion == "1" :
    print (nombre.upper())
elif opcion == "2":
    print (nombre.lower())
elif opcion == "3":
    print (nombre.title())