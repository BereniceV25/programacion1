#Ingresar un numero entero que represente una hora del día e informar:
#Si está entre las 7 y las 11 : "Es de mañana."

hora = int(input("Ingrese una hora del día (0-23): "))
match hora:
    case h if 7 <= h <= 11:
        print("Es de mañana.")
    case h if 0 <= h <= 23:
        print("No es de mañana.")
    case _:
        print("Error: Ingrese una hora válida entre 0 y 23.")