# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país 
# son los siguientes 
# Renta Tipo impositivo
# Menos de 100.000 5%
# Entre 100.000 y 200.000 15%
# Entre 200.000 y 350.000 20%
# Entre 350.000 y 600.000 30%
# Más de 600.000 45%
# Escribir un programa que pregunte al usuario su 
# renta anual y muestre por pantalla el tipo 
# impositivo que le corresponde:

rentaanual=int(input("Ingrese su renta anual: "))

if rentaanual < 100000:
    print("Tipo impositivo: 5%")
elif rentaanual < 200000:
    print("Tipo impositivo 15%")
elif rentaanual < 350000:
    print("Tipo impositivo 20%")
elif rentaanual < 600000:
    print("Tipo impositivo 30%")
else:
    print("Tipo impositivo: 45%")