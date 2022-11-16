# Imagina que acabas de abrir una nueva cuenta de caja de ahorros que te ofrece el 6% de 
# interés al anual. Estos ahorros debido a intereses, que no se cobran hasta finales 
# de año, se te añaden al balance final de tu caja de ahorros. Escribir un programa 
# que comience leyendo la cantidad de dinero depositada en la caja de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer año.
# Redondear cada cantidad a dos decimales.

plataDepositada=int(input("Plata depositada"))
interes=6

primeraño=plataDepositada+plataDepositada*interes/100
segundoaño=primeraño+primeraño*interes/100
terceraño=segundoaño+segundoaño*interes/100

print('El primer año usted tendrá ahorrados', round(primeraño, 2), 'pesos')
print('El segundo año usted tendrá', round(segundoaño, 2), 'pesos')
print('El tercer año usted tendrá ahorrados', round(terceraño, 2), 'pesos')
