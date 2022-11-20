##Ejercicio 10
##Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario

print(decimal_a_binario(79))