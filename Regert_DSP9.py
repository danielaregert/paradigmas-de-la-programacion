#Escribir un programa que pregunte al usuario una cantidad de dinero a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión.

dineroAInvertir=float(input("Ingrese una cantidad de dinero a invertir"))
interesAnual=float(input("Ingrese el interés anual de la inversión"))
años=int(input("Ingrese los años que invertirá"))

print("Capital final: " + str(round(dineroAInvertir * (interesAnual / 100 + 1) ** años, 2)))