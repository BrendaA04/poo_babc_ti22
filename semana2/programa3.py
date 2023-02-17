"""
    programa3
    Nombre:Brenda ABC
    Fecha: 24/01/2023
    Descripcion:
    invocando variables utilizando llaves.
    
"""
variable1= 10
variable2= 5
#print(variable1 + variable2 )  #  la primera lo suma y la otra lo concatena
print("{} + {} = {}".format(variable1,variable2, (variable1 + variable2))) #	Formatea cadenas de texto
#Crear diccionarios,Formatear cadenas de texto
print("{} - {} = {}".format(variable1,variable2, (variable1 - variable2)))#las llaves lo que hacen es formatear cadenas 

print("{} = {} * {}".format(( variable1 * variable2),variable1,variable2))#las llaves almacenan informacion no visible hasta que despues la ingrese el usuario

print("El resultado de dividir {} / {} = {}".format(variable1,variable2, (variable1 / variable2)))#imprime los datos almacenados depues de que se realice la operacion