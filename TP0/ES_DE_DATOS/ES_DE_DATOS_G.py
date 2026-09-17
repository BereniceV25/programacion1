#Ingresar un importe por input, transformarlo a número real (float), luego mostrar el
#importe ingresado, el 25% del mismo, y el importe con el descuento calculado.

importe = float(input("Ingrese el importe deseado: "))
importe_25= importe*0.25
resta_importes= importe-importe_25

print(f"El importe ingresado es: {importe}. El 25% del importe es: {importe_25}. La resta de ambos importes es: {resta_importes}")