# funciones de sumar, restar, multiplicacion y division
def sumar(a, b):
    return a + b
'''
    Qué hace: suma dos elementos.
    Args: a y b (números).
    Return: la suma de a y b.
'''

def restar(a, b):
    return a - b
'''
    Qué hace: resta dos elementos.
    Args: a y b (números).
    Return: la resta de a y b.
'''

def multiplicar(a, b):
    return a * b
'''
    Qué hace: multiplicacion de dos elementos.
    Args: a y b (números).
    Return: la multiplicacion de a y b.
'''

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b
'''
    Qué hace: division de dos elementos y verificación si b es 0
    Args: a y b (números).
    Return: la division de a y b, y mensaje si b es 0
'''
