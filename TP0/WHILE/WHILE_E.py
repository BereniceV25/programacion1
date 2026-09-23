#Ingresar cinco (5) números por input, e informar por consola la suma y el promedio de los números ingresados.

contador = 0
suma = 0

while contador < 5:
    numero = int(input(f"Ingrese el número {contador + 1} de 5: "))
    suma += numero
    contador += 1
promedio = suma / 5
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")