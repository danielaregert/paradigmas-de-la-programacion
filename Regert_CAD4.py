#Ejercicio 4 
# Los teléfonos de una empresa tienen el siguiente formato prefijo - Cod.área - número 
# donde el prefijo es el código del país +54, y la extensión tiene dos dígitos 
# (por ejemplo +54-11-98453629). 
# Escribir un programa que pregunte por un número de teléfono con este formato 
# y muestre por pantalla el número de teléfono sin el prefijo y el código de área.

telefono=input("Ingrese el teléfono")
endtel=len(telefono)
numerotelefono=telefono[7:endtel]

print(numerotelefono)
