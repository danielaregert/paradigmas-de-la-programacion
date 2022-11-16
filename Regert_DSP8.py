#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> 
# entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos
#  por el usuario, y <c> y <r> son el cociente y el resto de la división entera 
# respectivamente.

n = int(input("Ingrese un numero entero"))
m = int(input("Ingrese un segundo numero entero"))

c= int(n / m)
r= n % m

print(f'{n} dividido por {m} da un cociente de {c} y un resto de {r}')