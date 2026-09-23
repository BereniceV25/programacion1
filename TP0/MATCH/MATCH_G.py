#Ingresar dos números por input, transformarlos a entero (int).
#Luego seleccionar la opción:
#Sumar
#Restar
#Multiplicar
#Dividir (numero_uno / numero_dos)
#Mostar el resulto por consola.
#Ejemplo: "la suma es 750"

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
opcion = input("Seleccione una opción (Sumar, Restar, Multiplicar, Dividir): ").strip().capitalize()
match opcion:
    case "Sumar":
        resultado = numero_uno + numero_dos
        print(f"La suma es {resultado}")
    case "Restar":
        resultado = numero_uno - numero_dos
        print(f"La resta es {resultado}")
    case "Multiplicar":
        resultado = numero_uno * numero_dos
        print(f"La multiplicación es {resultado}")
    case "Dividir":
        if numero_dos != 0:
            resultado = numero_uno / numero_dos
            print(f"La división es {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    case _:
        print("Opción no válida.")