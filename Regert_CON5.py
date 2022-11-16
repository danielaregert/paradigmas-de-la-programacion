#Ejercicio 5 
# Para tributar un determinado impuesto se debe ser mayor de 16 años
#  y tener unos ingresos iguales o superiores a 360.000 $ mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

edad=int(input("Ingrese su edad"))
ingresos=int(input("Ingrese sus ingresos mensuales"))

if edad >= 16 and ingresos >= 360000:
    print("Usted puede tributar")
else:
    print("Usted no puede tributar")