# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números
# y otra que calcule el mínimo común múltiplo.



def mcd(num1,num2):

    divisiblesPornum1=[]
    divisiblesPornum2=[]
    divisiblesEnComun=[]
    for numeroP in [13,11,7,5,3,2]:
        if num1 % numeroP == 0:
            divisiblesPornum1.append(numeroP)
    for numeroP in [13,11,7,5,3,2]:
        if num2 % numeroP == 0:
            divisiblesPornum2.append(numeroP)
    for numero in divisiblesPornum1:
        if numero in divisiblesPornum2:
            divisiblesEnComun.append(numero)
    print("El MCD entre", num1, " y ", num2, "es: ", divisiblesEnComun[0])


mcd(225,300)



def mcm(num1,num2):
    multiplosnum1=[]
    multiplosnum2=[]
    multiplosencomun=[]

    for i in range(1,10):
        aux= i*num1
        multiplosnum1.append(aux)

    print(multiplosnum1)
    for i in range(1,10):
        aux=i*num2
        multiplosnum2.append(aux)
    print(multiplosnum2)

    for multiplo in multiplosnum1:
        if multiplo in multiplosnum2:
            multiplosencomun.append(multiplo)

    print(f'El mínimo múltiplo común entre {num1} y {num2} es {multiplosencomun[0]}')


mcm(12,18)