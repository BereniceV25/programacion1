#Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos
#los números impares desde 1 hasta el número ingresado

limite = int(input("Ingrese un número límite: "))
for numero in range(1, limite + 1):
    if numero % 2 != 0:
        print(numero)