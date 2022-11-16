# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario
# con su media, varianza y desviación estandard.

def cuadrados(lista):
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    return lista2

def estadistica(lista):
    dict = {}
    dict['media'] = sum(lista)/len(lista)
    dict['varianza'] = sum(cuadrados(lista))/len(lista)-dict['media']**2
    dict['desviacion tipica'] = dict['varianza']**0.5
    return dict
