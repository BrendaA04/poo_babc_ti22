"""
    programa5
    Nombre:Brenda ABC
    Fecha: 30/01/2023
    Descripcion:
    PERÍMETRO Y ÁREA DE UN TRIANGULO
    
"""
print(" ÁREA Y PERÍMETRO DEL TRIÁNGULO.")
##UN PRINT PARA QUE SE DE ESPACIO DE UNA LINEA 
print()

b = int(input("INGRESE BASE   : "))# esperar que el usuario introduzca un dato almacenar este dato en una variable.
h = int(input("INGRESE ALTURA : "))# esperar que el usuario introduzca un dato almacenar este dato en una variable.
l1 = int(input("INGRESE LA MEDIDA DE UN LADO : "))# esperar que el usuario introduzca un dato almacenar este dato en una variable.
l2 = int(input("INGRESA LA MEDIDA DE EL LADO QUE RESTA:"))# esperar que el usuario introduzca un dato almacenar este dato en una variable.
##PARA SACAR EL ÁREA 
A = (b*h)/2#se agrega la formula con la que se va a trabajar asignada en una variable
##PARA SACAR EL PERIMETRO
P = b + l1 + l2##se agrega la formula y se almacena en una variable 
print()
print("PERIMETRO : ", P)#va a imprimir el resultado de la operacion y te dara el perimetro 
print("ÁREA : ", A)#va a imprimir el area de acuerdo a los datos que se agregaron por el usuario
