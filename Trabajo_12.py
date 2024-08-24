#Programa que calcula el interes simple#
print("Programa que calcula el interes simple")

#Datos de entrada#
Capital=float(input("Ingrese el capital inicial"))
Tasa=float(input("ingrese la tasa de interes anual"))
Años=int(input("ingrese el numero de años"))

#procedimiento y datos de salida#
Interes=(Capital*Tasa*Años)
MontoTotal=Capital+Interes
print("El total acumulado despues de aplicar el interes simple es:", MontoTotal)
