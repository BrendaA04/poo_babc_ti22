"""
    programa5
    Nombre:Brenda ABC
    Fecha: 31/01/2023
    Descripcion:
    PERÍMETRO Y ÁREA DE UN CIRCULO Y UN CUADRADO
    
"""
PI = 3.1416
print()
lado_1 = int(input("INGRESE LA MEDIDA DEL PRIMER LADO : "))## esperar que el usuario introduzca un dato almacenar este dato en una variable.

perimetro_cuadrado = lado_1*4#se establece la operacion que se va a realizar 
print()
print ("El perímetro de un cuadrado con la medida de sus lados: ",lado_1, ("es: ") , perimetro_cuadrado)#una linea de texto con resultado de la operacion 

area_cuadrado = lado_1*lado_1#se integra la operacion que se va a realizar 
print()
print ("El área de un cuadrado con la medida de sus lados: ",lado_1, ("es: ") , area_cuadrado)#imprime una linea de texto con el resultado de la operacion
print()
##perimetro y área de un circulo

radio_circulo = int (input("ingresa la medida de la circunferencia de el círculo: ")) #pide al usuario que integre los datos solicitados 
##ÁREA DE DEL CIRCULO
area_circulo = (PI*radio_circulo**2)#se integra la formula a trabajar
print()
print ("El área de un círculo con un radio de: ",radio_circulo, ("es: ") , area_circulo)#imprime una linea de texto con el resultado de la operacion
##ESPACIO
print()
##PERÍMETRO DEL CIRCULO
perimetro_circulo = (2*PI*radio_circulo)#pide al usuario que integre los datos solicitados 
print()
print("El perímetro de un círculo con un radio de",radio_circulo,("es: "),perimetro_circulo)#imprime una linea de texto con el resultado de la operacion
print()
print("Gracias por utilizar este programa")#linea que imprime un texto al finalizarlo 
print()