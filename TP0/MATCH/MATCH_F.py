#Ingresar un número entero que represente una hora del día e informar:
#Si está entre las 7 y las 11 : "Es de mañana."
#Si está entre las 12 y las 19 : "Es de tarde."
#Si está entre las 20 y las 23 o entre las 0 y las 6 : "Es de noche."
#Si no está entre las 0 y las 23 : "la hora no existe."

hora = int(input("Ingrese una hora del día (0 a 23): "))
match hora:
    case h if 7 <= h <= 11:
        print("Es de mañana.")
    case h if 12 <= h <= 19:
        print("Es de tarde.")
    case h if (20 <= h <= 23) or (0 <= h <= 6):
        print("Es de noche.")
    case _:
        print("La hora no existe.")