#Programa para sacar el promedio#
print("Programa para sacar promedio")
totalNum=int(input("De cuantos numero quieres sacar el promedio"))
Contador=0

#suma de el input#
for i in range (totalNum):
    Numero=int(input("ingrese un numero"))
    Contador =Contador+Numero 
Promedio= Contador/totalNum

#DATOS DE SALIDA#
print("El promedio es igual",Promedio)