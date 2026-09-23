#Ingresar un mes por input e informar:
#Si es Febrero: " Este mes no tiene más de 29 días."
#Si no es Febrero: "Este mes tiene 30 o más días."

mes = input("Ingrese un mes: ").strip().capitalize()

match mes:
    case "Febrero":
        print("Este mes no tiene más de 29 días.")
    case "Enero" | "Marzo" | "Abril" | "Mayo" | "Junio" | "Julio" | "Agosto" | "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Este mes tiene 30 o más días.")
    case _:
        print("Error: El mes ingresado no es válido.")