# Ejercicio 2 
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas 
# y minúsculas.

contraseñaguardada="pepito"

contraseñaingresada=input("introduzca su contraseña")

if contraseñaguardada == contraseñaingresada.lower():
    print("contraseña correcta")
else:
    print("contraseña incorrecta")
