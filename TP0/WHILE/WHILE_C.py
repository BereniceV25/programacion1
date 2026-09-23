#Ingresar un número por input, y mostrarlo por consola. El número ingresado debe
#estar comprendido entre 0 y 9 inclusive, caso contrario volver a pedirlo hasta que el
#número ingresado esté dentro de ese rango

numero = int(input("Ingrese un número entre 0 y 9 inclusive: "))
while numero < 0 or numero > 9:
    print("Error: El número ingresado no está en el rango permitido.")
    numero = int(input("Por favor, ingrese un número entre 0 y 9: "))
print(f"Número válido ingresado: {numero}")