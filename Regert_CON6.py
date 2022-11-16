#Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y determine en qué grupo están


nombre=input("Ingrese su nombre").lower()
sexo=input("Ingrese H si es hombre, M si es mujer").lower()

if nombre[0] < "m" and sexo == "m" or nombre[0] > "n" and sexo == "h":
    print("Usted está en grupo A")
else:
    print("Usted está en grupo B")

