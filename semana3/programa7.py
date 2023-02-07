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
if numero_1 > numero_2:  
    print(numero_1)
elif numero_2 > numero_1:
    print(numero_2)
else:
    print(None)