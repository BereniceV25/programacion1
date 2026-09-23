#Ingresar una letra por input, validar que la misma sea "F" o "M", caso contrario
#volver a pedirla. Una vez validado el ingreso de la letra, mostrar por consola:
#Si la letra ingresada es "F": “FEMERNINO”. Si la letra ingresa es "M": “MASCULINO”.

letra = input("Ingrese género (F o M): ").strip().upper()
while letra != "F" and letra != "M":
    print("Error: Ingreso inválido.")
    letra = input("Por favor, ingrese 'F' o 'M': ").strip().upper()
if letra == "F":
    print("FEMENINO")
else:
    print("MASCULINO")