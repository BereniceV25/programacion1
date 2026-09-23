#Ingresar un mes por input e informar:
#Si tiene 28 días.
#Si tiene 30 días.
#Si tiene 31 días
mes = input("Ingrese un mes: ").strip().capitalize()

match mes:
    case "Febrero":
        print("Tiene 28 días (o 29 en año bisiesto).")
    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
        print("Tiene 30 días.")
    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
        print("Tiene 31 días.")
    case _:
        print("Error: El mes ingresado no es válido.")