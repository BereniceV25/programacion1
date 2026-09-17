barbijo_mas_caro_precio = 0
barbijo_mas_caro_cantidad = 0
barbijo_mas_caro_fabricante = ""
ingreso_barbijo = False
mayor_cantidad_unidades = 0
fabricante_mas_unidades = ""
total_unidades_jabones = 0

for i in range(5):
    print(f"\n--- CARGA DE PRODUCTO {i + 1} DE 5 ---")
    tipo = input("Tipo (barbijo/jabon/alcohol): ").lower()
    while tipo not in ["barbijo", "jabon", "alcohol"]:
        print("Error: Tipo inválido. Debe ser 'barbijo', 'jabon' o 'alcohol'.")
        tipo = input("Tipo (barbijo/jabon/alcohol): ").lower()
    while True:
        try:
            precio = float(input("Precio (100 a 300): "))
            if 100 <= precio <= 300:
                break
            else:
                print("Error: El precio debe estar entre 100 y 300.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    while True:
        try:
            unidades = int(input("Cantidad de unidades (1 a 1000): "))
            if 1 <= unidades <= 1000:
                break
            else:
                print("Error: Las unidades deben estar entre 1 y 1000.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    marca = input("Marca: ")
    fabricante = input("Fabricante: ")
    if tipo == "barbijo":
        if not ingreso_barbijo or precio > barbijo_mas_caro_precio:
            barbijo_mas_caro_precio = precio
            barbijo_mas_caro_cantidad = unidades
            barbijo_mas_caro_fabricante = fabricante
            ingreso_barbijo = True
    if i == 0 or unidades > mayor_cantidad_unidades:
        mayor_cantidad_unidades = unidades
        fabricante_mas_unidades = fabricante
    if tipo == "jabon":
        total_unidades_jabones += unidades
print("\n" + "=" * 50)
if ingreso_barbijo:
    print(f"El mas caro de los barbijos tiene una cantidad de: {barbijo_mas_caro_cantidad} unidades y es fabricado por: {barbijo_mas_caro_fabricante}")
else:
    print("No se ingresaron barbijos.")
print(f"El item con mas unidades es fabricado por: {fabricante_mas_unidades} y la cantidad es: {mayor_cantidad_unidades}")
print(f"La cantidad de jabones es: {total_unidades_jabones}")
print("Gracias por usar el programa")