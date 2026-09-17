#Al ingresar una edad por input, se debe informar si la persona es adolescente, edad
#entre 13 y 17 años (inclusive), caso contrario, no informar nada. 

edad = int(input("Ingrese su edad: "))
if edad >= 13 and edad <= 17:
    print("Es adolescente")