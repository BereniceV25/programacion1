#Ingresar por input un número mayor a 0 (cero), y mostrar ese número por consola.
#Repetir la operación una y otra vez, hasta que ingresemos (cero), en ese caso finalizar la ejecución del programa.

for _ in range(1000000):
    numero = int(input("Ingrese un número mayor a 0 (0 para salir): "))
    
    if numero == 0:
        break
    elif numero < 0:
        print("Error: El número debe ser mayor a 0.")
    else:
        print(numero)