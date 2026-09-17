#Al ingresar una edad por input se debe informar si la persona es mayor de edad,
#caso contrario, informar que es un menor de edad. 

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")