def factorial(numero):
    resultado = 1
    i = 1 
    while i <= numero:  
        resultado = resultado * i
        i += 1  
    return resultado
print(factorial(3))