# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio edu.ar.

correo=input("¿Cuál es su correo electrónico?")

ubicacion=0
for letra in correo:
    ubicacion+=1
    if letra == "@":
        break

correo2= correo[0:ubicacion]
correo3= correo2 + "edu.ar"

print(correo3)
