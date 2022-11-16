# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad)

edad=int(input("ingrese su edad"))
contador=0

for i in range(edad):
    contador+=1
    print(contador)

