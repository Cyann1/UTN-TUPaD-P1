contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud = len(contrasena)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
