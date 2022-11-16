#Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.

f=input("Ingrese algo: ")

while f != "salir":
    print(f)
    f=input("Ingrese algo: ")


