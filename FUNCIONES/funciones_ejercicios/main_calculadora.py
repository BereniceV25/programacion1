from calculadora import *
#el * despues de import significa que se llaman todas las funciones de ese modulo

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamamos a cada función y mostramos los resultados
print(f"Suma: {sumar(num1, num2)}")
print(f"Resta: {restar(num1, num2)}")
print(f"Multiplicación: {multiplicar(num1, num2)}")
print(f"División: {dividir(num1, num2)}")