#Ejercicio 10 
# Escribir un programa que pregunte por consola por los productos de una canasta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

lista=input("Ingrese una lista de productos que compró separados por comas")

palabras=lista.split(",")

for palabra in palabras:
    print(palabra.strip())

#strip: quitar espacios segun argumento
#split corta las palabras segun un separador