def sumar(numero_a: int, numero_b: int) -> int:
    """Funcion que se encarga de sumar dos números enteros.

    ARGS:
    numero_a (int): primer número
    numero_b (int): segundo número

    Returns:
    int: devuelve la suma entre estos dos números
    """
    suma = numero_a + numero_b
    return suma

numero_a = int(input("Ingrese primer número: "))
numero_b = int(input("Ingrese segundo número: "))

resultado = sumar(numero_a, numero_b)
print(f"La suma es: {resultado}")