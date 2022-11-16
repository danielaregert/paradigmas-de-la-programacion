# Una panadería vende facturas a $20 cada una. Las facturas que no son del día tiene 
# un descuento del 60%. Escribir un programa que comience leyendo cantidad de facturas
# vendidas que no son del día. Después el programa debe mostrar el precio habitual 
# de una factura, el descuento que se le hace por no ser fresca y el precio final total

facturasViejasVendidas= int(input("¿Cuántas facturas vendidas que no son del día?"))

factura=20
descuento=factura*0.6
facturavieja=factura-descuento

print("El precio habitual de una factura es", factura)
print("El descuento hecho por ser vieja es", descuento)
print("El precio final total es", facturavieja)
print( facturasViejasVendidas, "facturas no del día se vendieron a", facturavieja*facturasViejasVendidas, "pesos")


