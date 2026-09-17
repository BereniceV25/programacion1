#Ingresar dos números por input, transformarlos a enteros (int), realizar la operación aritmética de división, pero para obtener y mostrar el resto (operador módulo) entre
#el dividendo (numero_uno) y el divisor (numero_dos). Ejemplo: "El resto es 0."

numero_A = int(input("Ingrese el primer número: "))
numero_B = int(input("Ingrese el segundo número: "))
resto = numero_A % numero_B

print(f"El resto es {resto}.")