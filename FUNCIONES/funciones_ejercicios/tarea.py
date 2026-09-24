def es_alfabetico(caracter: str) -> bool:
    '''
    Verifica si un carácter es una letra usando rangos ASCII:
    'A'-'Z' (65-90) o 'a'-'z' (97-122).
    '''
    retorno = False
    if len(caracter) == 1:
        codigo = ord(caracter)
        if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
            retorno = True
    return retorno

def es_cadena_alfabetica(cadena: str) -> bool:
    '''
    Verifica si toda la cadena está compuesta únicamente por letras.
    '''
    if len(cadena) == 0:
        return False
        
    retorno = True
    for caracter in cadena:
        if es_alfabetico(caracter) == False:
            retorno = False
            break
            
    return retorno

def es_entero(cadena: str) -> bool:
    '''
    Verifica si la cadena es un entero válido (admite signo negativo '-' al inicio).
    '''
    if len(cadena) == 0:
        return False
        
    if cadena[0] == "-":
        cadena = cadena[1:]
        if len(cadena) == 0: 
            return False

    retorno = True
    for caracter in cadena:
        if (ord(caracter) >= 48 and ord(caracter) <= 57) == False:
            retorno = False
            break
            
    return retorno

def es_real(cadena: str) -> bool:
    '''
    Verifica si es un número decimal (admite '-' al inicio y exactamente un punto '.').
    '''
    if len(cadena) == 0:
        return False

    if cadena[0] == "-":
        cadena = cadena[1:]
        if len(cadena) == 0:
            return False

    puntos = 0
    retorno = True

    for caracter in cadena:
        if caracter == ".":
            puntos += 1
            if puntos > 1: 
                retorno = False
                break
        elif (ord(caracter) >= 48 and ord(caracter) <= 57) == False:
            retorno = False
            break

    if cadena.endswith("."):
        retorno = False

    return retorno