#funciones de suma, resta, multiplicacion y division
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


# pedimos dos numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# llamamos a la función y generamos los resultados
print(f"Suma: {sumar(num1, num2)}")
print(f"Resta: {restar(num1, num2)}")
print(f"Multiplicación: {multiplicar(num1, num2)}")
print(f"División: {dividir(num1, num2)}")