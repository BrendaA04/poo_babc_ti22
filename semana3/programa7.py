"""
    programa5
    Nombre:Brenda ABC
    Fecha: 01/02/2023
    Descripcion:
    Comparar 2 numeros enteros e imprimir el numero mayor
    
"""
print("Comparar 2 números enteros e imprimir el número mayor")
print()
##SE LE PIDE AL USUARIO QUE INGRESE EL VALOR DE DOS NUMEROS POSITIVOS O NEGATIVOS
numero_1 = int(input("INGRESE EL VALOR DE EL PRIMER NÚMERO : "))
numero_2 = int(input("INGRESE EL VALOR DE EL SEGUNDO NÚMERO : "))
#SE HACE LA COMPARACION DE LOS NUMEROS INGRESADOS Y TE DARA EL VALOR DE QUE NUMERO ES MAYOR 
if numero_1 > numero_2:  #permite ejecutar el código Python si se cumple una condición.
    print(numero_1)#si se cumple la condicion antes establecida se imprime esta linea 
elif numero_2 > numero_1: #se utiliza para comprobar múltiples condiciones si una condición es falsa, evalúa múltiples condiciones
    print(numero_2)#si se cumple la condicion antes establecida se imprime esta linea 
else:  ##Ejecutan una o varias sentencias de manera condicional. Puede utilizar una sintaxis de una sola línea o varias líneas en un bloque.
    print(None)#si se no cumple la condicion antes establecida se imprime esta linea 