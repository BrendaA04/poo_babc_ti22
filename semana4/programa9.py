"""
    programa9
    Nombre:Brenda ABC
    Fecha: 08/02/2023
    Descripcion:
    Programa que por medio de def definimos mayor y None(iguales)
    
"""

def mayor(numero1,numero2): #constructor de la clase profesor
    if numero1 > numero2: #if es para establecer una condicion y que se ejecute cuando se cumple 
        print(numero1) #imprime el resultado
    elif numero2 > numero1: #se utiliza para comprobar múltiples condiciones si una condición es falsa
        print(numero2) #imprime el resultado
    else: #Ejecutan una o varias sentencias de manera condicional
        print(None) #imprime el resultado

mayor (3,2) #se 
mayor (2,3)
mayor (3,3)

##programa que por medio de def definimos mayor

def mayor(numero1:int,numero2:int)->int: #constructor de la clase profesor
    mayor=None
    if numero1 > numero2:#if es para establecer una condicion y que se ejecute cuando se cumple 
        mayor=numero1
    elif numero2 > numero1:#se utiliza para comprobar múltiples condiciones si una condición es falsa
        mayor = numero2
    else: #Ejecutan una o varias sentencias de manera condicional
        mayor=None
    return mayor

print(mayor(3,2))
print(mayor(2,3))
print(mayor(3,3))






