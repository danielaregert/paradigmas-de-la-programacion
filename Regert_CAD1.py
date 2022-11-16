#Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas el nombre del usuario
# tantas veces como el número introducido.

nombreUsuario=input("Ingrese un nombre de usuario")
numeroEntero=int(input("Ingrese un numero entero"))

for i in range(numeroEntero):
    print(nombreUsuario)