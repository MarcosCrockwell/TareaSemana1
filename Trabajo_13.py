#Programa que calcula el volumen y el area de una esfera#
print("Programa que calcula el volumen y el area de una esfera")

#Datos de entrada#
Radio=float(input("ingrese el radio de la esfera"))

#Procedimiento y Datos de salida#
Area=4*(3.14*(Radio**2))
Volumen=3/4*(3.14*(Radio**3))

print("El area de la esfera es",Area, "y el volumen es",Volumen)