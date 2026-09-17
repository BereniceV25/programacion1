#ejercicio while G
#Ingresar tantos números por input como el usuario desee, e informar por consola la
#suma de los números positivos, y la multiplicación de los números negativos
suma_positivos = 0
producto_negativos = 1
ingreso_positivo = False
ingreso_negativo = False
continuar = "s"
while continuar.lower() == "s":
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            break 
        except ValueError:
            print("Error: El valor ingresado no es un número válido. Intente nuevamente.")
    if numero > 0:
        suma_positivos += numero
        ingreso_positivo = True
    elif numero < 0:
        producto_negativos *= numero
        ingreso_negativo = True
    continuar = input("¿Desea ingresar otro número? (s/n): ")
    while continuar.lower() not in ["s", "n"]:
        print("Opción incorrecta. Debe ingresar 's' para sí o 'n' para no.")
        continuar = input("¿Desea ingresar otro número? (s/n): ")
print("\n--- RESULTADOS ---") # \n significa un salto de linea 
if ingreso_positivo:
    print(f"Suma de números positivos: {suma_positivos}")
else:
    print("No se ingresaron números positivos.")
if ingreso_negativo:
    print(f"Multiplicación de números negativos: {producto_negativos}")
else:
    print("No se ingresaron números negativos.")