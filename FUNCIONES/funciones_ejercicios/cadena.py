def es_cadena_numerica_ascii(cadena):
    '''
    Qué hace: Verifica si todos los caracteres de una cadena son dígitos numéricos en ASCII (48-57).
    Args: cadena (str).
    Return: True si toda la cadena es numérica, False en caso contrario.
    '''
    if len(cadena) == 0:
        return False  

    for caracter in cadena:
        codigo_ascii = ord(caracter)
        if codigo_ascii < 48 or codigo_ascii > 57:
            return False
            
    return True  