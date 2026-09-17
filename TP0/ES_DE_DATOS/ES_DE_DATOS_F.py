#Ingresar un importe por input, transformarlo a número real (float), luego mostrar el importe ingresado, el 10% del mismo, y el importe con el incremento calculado.

importe = float(input("Ingrese el importe deseado: "))
importe_10= importe*0.1
suma_importes= importe+importe_10

print(f"El importe ingresado es: {importe}. El 10% del importe es: {importe_10}. La suma de ambos importes es: {suma_importes}")