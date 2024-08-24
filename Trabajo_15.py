#Programa que calcula el impuesto sobre la compra#
print("Programa que calcula el impuesto sobre la compra")

#Datos de entrada#
Compra=float(input("ingrese el total de la compra"))
Tasa=float(input("ingrese la tasa de impuesto"))
Tasa=Tasa/100

#Datos de salida y procedimiento#
Impuesto=Compra*Tasa
Total=Compra+Impuesto
print("El total a pagar es",Total)