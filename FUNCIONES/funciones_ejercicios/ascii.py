def es_numero_ascii(caracter):
    '''
    Qué hace: Determina si un carácter ingresado corresponde a un número entre 0 y 9 en ASCII.
    Args: caracter (str).
    Return: True si el código ASCII está entre 48 y 57, False en caso contrario.
    '''
    if len(caracter) == 1:
        codigo_ascii = ord(caracter)
        if 48 <= codigo_ascii <= 57:
            return True
            
    return False