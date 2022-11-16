#Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
# introducida empezando por la última.

palabra=(input("Ingrese una palabra: "))
largo=len(palabra)-1
for i in range(largo,-1,-1):
    print(palabra[i])

