#Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

numero1= int(input("Ingrese un numero: "))
numero2= int(input("Ingrese otro numero: "))

try:
    division= numero1 / numero2
    print(int(division))
except:
    print("Error")
