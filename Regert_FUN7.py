#Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista 
# y devuelva otra lista con sus cuadrados

def cuadradosDeUnaLista(lista):
    listacuadrados=[]
    for i in lista:
        listacuadrados.append(i**2)
    return listacuadrados

