#Al ingresar un número por input, evaluar si el mismo es 1980, si es así mostrar el mensaje "Este año se creó del videojuego Pac-Man" por consola
# Pedimos el año al usuario y lo convertimos a entero
anio = int(input("Ingrese un año: "))

if anio == 1980:
    print("Este año se creó el videojuego Pac-Man")
elif anio > 1980:
    print("El año ingresado es posterior a la creación de Pac-Man.")
else:
    print("El año ingresado es anterior a la creación de Pac-Man.")