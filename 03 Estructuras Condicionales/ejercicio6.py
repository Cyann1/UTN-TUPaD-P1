from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista) 

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda :
    print ("Sesgo positivo o a la derecha")
elif media < mediana < moda :
    print ("Sesgo negativo o a la izquierda")
elif media == mediana == moda :
    print ("Sin sesgo:")

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)