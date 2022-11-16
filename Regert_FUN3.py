#Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp