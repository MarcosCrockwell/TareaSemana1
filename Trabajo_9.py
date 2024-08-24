#Programa que determina si un año es bisiesto#
print("Programa que determina si un año es bisiesto")

#Variables de entrada
Año=int(input("Elige un año para determinar si es bisiesto"))

#Procedimiento y datos de salida
if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400==0):
    print("El año es bisiestos")
else:
    print("El año no es bisiestos")    