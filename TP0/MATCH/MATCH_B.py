#Ingresar un mes por input e informar por consola:
#Si estamos en Invierno: "Abrigate que hace frio."
#Si aún no llego el Invierno: "Falta para el invierno."
#Si ya paso el Invierno: "Ya pasamos el frio, ahora calor!"
#Aclaración: Se debe tomar a Julio y Agosto como los meses de invierno

mes = input("Ingrese un mes: ").strip().capitalize()
match mes:
    case "Julio" | "Agosto":
        print("Abrigate que hace frio.")
    case "Enero" | "Febrero" | "Marzo" | "Abril" | "Mayo" | "Junio":
        print("Falta para el invierno.")
    case "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Ya pasamos el frio, ahora calor!")
    case _:
        print("Mes no válido.")