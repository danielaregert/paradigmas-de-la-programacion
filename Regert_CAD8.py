# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en pesos 
# con dos decimales y muestre por pantalla el número de pesos y el número de céntimos
# del precio introducido

precio=input("Ingrese el precio de un producto en pesos")

contador=0

for numero in precio:
    contador+=1
    if numero == "," or numero == ".":
        break

largoprecio=len(precio)

print("El numero ingresado es", precio)

pesos= precio[0:contador-1]
centimos=precio[contador: largoprecio]

print(f'Los pesos son {pesos}')
print(f'Los céntimos son {centimos}')