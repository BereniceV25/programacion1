def calcular_factorial(numero):
    if numero ==0:
        resultado=1
    else:
        resultado=numero*calcular_factorial(numero-1)
    return resultado

num = int(input("Ingrese un número para calcular su factorial: "))
factorial = calcular_factorial(num)

# 3. Mostrar el resultado por pantalla
print(f"El factorial de {num} es: {factorial}")