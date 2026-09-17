#Ingresar un mes por input e informar por consola:
#Si es Enero: "Que comiences bien el año!"
#Si es Marzo: "A clases!"
#Si es Julio: "Se vienen las vacaciones!"
#Si es Diciembre: "Felices fiesta!" 

#capitalize(): Transforma la entrada para que la primera letra sea mayúscula (ejemplo: si ingresan "enero", lo convierte a "Enero" para coincidir exactamente con el caso).
#strip(): Quita espacios en blanco innecesarios al inicio o final del texto.

mes = input("Ingrese un mes: ").strip().capitalize()
match mes:
    case "Enero":
        print("Que comiences bien el año!")
    case "Marzo":
        print("A clases!")
    case "Julio":
        print("Se vienen las vacaciones!")
    case "Diciembre":
        print("Felices fiestas!")