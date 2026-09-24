from cadena import *

entrada = input("Ingrese una cadena de texto o número: ")

if es_cadena_numerica_ascii(entrada):
    print(f"La cadena '{entrada}' ES un número válido.")
    
    numero_entero = int(entrada)
    print(f"Convertido a entero: {numero_entero}")
else:
    print(f"La cadena '{entrada}' NO es un número válido.")