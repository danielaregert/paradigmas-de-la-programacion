#Ejercicio 5 
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
# y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión cada año que dura la inversión.

cantidad=float(input("¿Cantidad a invertir?"))
interes=float(input("¿Interés anual?"))
años=int(input("¿Años?"))

año=0
aumentocapital=0
for i in range(años):
    aumentocapital+=cantidad+cantidad*interes/100
    año+=1
    print(f'Su capital aumentará a {aumentocapital} el año {año} ')