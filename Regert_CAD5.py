#Ejercicio 5 
# Escribir un programa que pida al usuario que introduzca una frase en la consola 
# y muestre por pantalla la frase invertida.

frase=input("Introduzca una frase")

def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

fraseinvertida=invertir_cadena_manual(frase)
print(fraseinvertida)