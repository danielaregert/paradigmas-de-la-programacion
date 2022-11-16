#Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseñaguardada="Roquefort"

contraseñaingresada=input("Ingrese contraseña: ")
while contraseñaingresada != contraseñaguardada:
    print("contraseña incorrecta")
    contraseñaingresada=input("Ingrese contraseña: ")

print("Contraseña correcta. Fin del programa")

