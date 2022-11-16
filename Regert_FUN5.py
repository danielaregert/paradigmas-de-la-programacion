# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen
# de un cilindro usando la primera función.

def areaDeUnCirculo(radio):
    return 3.14*radio**2

def volumenDeUnCilindro(altura, radio):
    return areaDeUnCirculo(radio)*altura
