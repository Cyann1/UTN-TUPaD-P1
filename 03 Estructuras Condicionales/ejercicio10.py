hemisferio = str(input ("Ingrese si se encuentra en el norte o sur: "))
mes = int(input ("Ingrese el mes actual (1-12): "))
año = int(input ("Ingrese el año actual : "))
dia = int(input ("Ingrese que dia es hoy (1-31): "))

fecha = (mes, dia)

if hemisferio == "norte":
    if fecha >= (12, 21) or fecha <= (3, 20):
        estacion = "Invierno"
    elif fecha >= (3, 21) and fecha <= (6, 20):
        estacion = "Primavera"
    elif fecha >= (6, 21) and fecha <= (9, 20):
        estacion = "Verano"
    elif fecha >= (9, 21) and fecha <= (12, 20):
        estacion = "Otoño"
elif hemisferio == "sur":
    if fecha >= (12, 21) or fecha <= (3, 20):
        estacion = "Verano"
    elif fecha >= (3, 21) and fecha <= (6, 20):
        estacion = "Otoño"
    elif fecha >= (6, 21) and fecha <= (9, 20):
        estacion = "Invierno"
    elif fecha >= (9, 21) and fecha <= (12, 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostrar el resultado
print(f"Fecha ingresada: {dia}/{mes}/{año}")
print(f"Estás en {estacion}.")