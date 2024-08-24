#Programa que determina que tipo de triangulo es#
print("Programa que determina que tipo de triangulo es")

#Datos de entrada#
Lado1=float(input("ingrese el lado 1"))
Lado2=float(input("ingrese el lado 2"))
Lado3=float(input("ingrese el lado 3"))

#Procedimiento y datos de salida#
if(Lado1==Lado2==Lado3):
    print("El triangulo es equilatero")
elif(Lado1 !=Lado2 !=Lado3):
    print("El triangulo es escaleno")
elif(Lado1==Lado2) or (Lado1==Lado3) or (Lado2==Lado3):
    print("El triangulo es isoceles")