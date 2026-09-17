#Al ingresar una edad por input se debe informar por consola si la persona es mayor
#de edad, caso contrario no informar nada

# Pedimos la edad y la convertimos a número entero
edad = int(input("Ingrese su edad: "))

# Evaluamos si es mayor de edad (18 años o más)
if edad >= 18:
    print("Es mayor de edad")