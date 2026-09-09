#ejercicio while F
#Ingresar tantos números por input como el usuario desee, e informar por consola la
#suma y el promedio de los números ingresados.
suma_total = 0
cantidad_numeros = 0
continuar = "s"

while continuar.lower() == "s":
    numero = float(input("Ingrese un número: "))
    suma_total += numero
    cantidad_numeros += 1
    continuar = input("¿Desea ingresar otro número? (s/n): ")
    while continuar.lower() not in ["s", "n"]:
        print("Opción incorrecta. Debe ingresar 's' para sí o 'n' para no.")
        continuar = input("¿Desea ingresar otro número? (s/n): ")
if cantidad_numeros > 0:
    promedio = suma_total / cantidad_numeros
    print("\n--- RESULTADOS ---")
    print(f"Suma total: {suma_total}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("\nNo se ingresó ningún número.")
