from ascii import *

entrada = input("Ingrese un carácter: ")

if es_numero_ascii(entrada):
    print(f"El carácter '{entrada}' es un número entre 0 y 9 en ASCII.")
else:
    print(f"El carácter '{entrada}' NO es un valor del 0 al 9 en ASCII.")