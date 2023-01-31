"""
    programa5
    Nombre:Brenda ABC
    Fecha: 31/01/2023
    Descripcion:
    PERÍMETRO Y ÁREA DE UN CIRCULO Y UN CUADRADO
    
"""
PI = 3.1416
print()
lado_1 = int(input("INGRESE LA MEDIDA DEL PRIMER LADO : "))

perimetro_cuadrado = lado_1*4
print()
print ("El perímetro de un cuadrado con la medida de sus lados: ",lado_1, ("es: ") , perimetro_cuadrado)

area_cuadrado = lado_1*lado_1
print()
print ("El área de un cuadrado con la medida de sus lados: ",lado_1, ("es: ") , area_cuadrado)
print()
##perimetro y área de un circulo

radio_circulo = int (input("ingresa la medida de la circunferencia de el círculo: "))
##ÁREA DE DEL CIRCULO
area_circulo = (PI*radio_circulo**2)
print()
print ("El área de un círculo con un radio de: ",radio_circulo, ("es: ") , area_circulo)
##ESPACIO
print()
##PERÍMETRO DEL CIRCULO
perimetro_circulo = (2*PI*radio_circulo)
print()
print("El perímetro de un círculo con un radio de",radio_circulo,("es: "),perimetro_circulo)
print()
print("Gracias por utilizar este programa")
print()