"""
    programa9
    Nombre:Brenda ABC
    Fecha: 08/02/2023
    Descripcion:
    Programa que por medio de def definimos mayor y None(iguales)
    
"""

def mayor(numero1,numero2):
    if numero1 > numero2:
        print(numero1)
    elif numero2 > numero1:
        print(numero2)
    else:
        print(None)

mayor (3,2)
mayor (2,3)
mayor (3,3)

##programa que por medio de def definimos mayor

def mayor(numero1:int,numero2:int)->int:
    mayor=None
    if numero1 > numero2:
        mayor=numero1
    elif numero2 > numero1:
        mayor = numero2
    else:
        mayor=None
    return mayor

print(mayor(3,2))
print(mayor(2,3))
print(mayor(3,3))






