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

b = int(input("INGRESE BASE   : "))
h = int(input("INGRESE ALTURA : "))
l1 = int(input("INGRESE LA MEDIDA DE UN LADO : "))
l2 = int(input("INGRESA LA MEDIDA DE EL LADO QUE RESTA:"))
##PARA SACAR EL ÁREA 
A = (b*h)/2
##PARA SACAR EL PERIMETRO
P = b + l1 + l2
print()
print("PERIMETRO : ", P)
print("ÁREA : ", A)
