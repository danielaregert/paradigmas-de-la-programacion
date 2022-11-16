#Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def mediaLista(lista):
    acum=0
    for i in lista:
        acum+=i
    return acum/len(lista)
