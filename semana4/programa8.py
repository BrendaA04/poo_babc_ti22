"""
    programa8
    Nombre:Brenda ABC
    Fecha: 07/02/2023
    Descripcion:
    PROGRAMA DE 11 FORMAS DIFERENTES PARA USAR IF
    
"""
print()
n1 = int(input("Inresa N1: "))#se le  pide al usuario que ingrese los datos, y los almacena en la variable
n2 = int(input("Ingresa N2: "))#se le  pide al usuario que ingrese los datos, y los almacena en la variable
print()
#PROGRAMA DE 11 FORMAS DIFERENTES PARA USAR IF
print("Forma numero 1")#imprime el texto entre comillas
if n1 > n2: #if es para establecer una condicion y que se ejecute cuando se cumple 
    print(n1)#imprime el recultado de la condicion si se cumple
if n2 > n1:#if es para establecer una condicion y que se ejecute cuando se cumple
    print(n2)#imprime el recultado de la condicion si se cumple
if n1 == n2:#lo utilizamos para realizar una comparación entre dos valores y la salida de esta comparación
    print(None)##imprime el recultado de la condicion si se cumple

##USO DE IF E IGUAL
print( "Forma numero 2" )#imprime el texto entre comillas

if n2 > n1:#if es para establecer una condicion y que se ejecute cuando se cumple 
    print(n2)#imprime el recultado de la condicion si se cumple
if n1 > n2:#if es para establecer una condicion y que se ejecute cuando se cumple
    print(n1)#imprime el recultado de la condicion si se cumple
if n2 == n1:#lo utilizamos para realizar una comparación entre dos valores y la salida de esta comparación
    print(None)#imprime el recultado de la condicion si se cumple

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 3" )#imprime el texto entre comillas
#if y else son en: (en caso (contrario) de)
if n1 > n2:#if es para establecer una condicion y que se ejecute cuando se cumple 
    print(n1)#imprime el recultado de la condicion si se cumple
elif n2 > n1:#se utiliza para comprobar múltiples condiciones si una condición es falsa
    print(n2)#imprime el recultado de la condicion si se cumple
else:#Ejecutan una o varias sentencias de manera condicional
    print(None)#imprime el recultado de la condicion si se cumple

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 4" )

if n1 < n2:#if es para establecer una condicion y que se ejecute cuando se cumple 
    print(n2)
elif n2 < n1:#se utiliza para comprobar múltiples condiciones si una condición es falsa
    print(n1)
else:#Ejecutan una o varias sentencias de manera condicional
    print(None)#imprime el recultado de la condicion si se cumple


##USO DE IF E IGUAL
print( "Forma numero 5" )

if n2 < n1:#Si la expresión evaluada, resulta ser verdadera, entonces ejecuta una vez el código en la expresión 
    print(n1)
if n1 < n2:#Si la expresión evaluada, resulta ser verdadera, entonces ejecuta una vez el código en la expresión 
    print(n2)
if n1 == n2:#Si la expresión evaluada, resulta ser verdadera, entonces ejecuta una vez el código en la expresión 
    print(None)

##USO DE IF Y ELIF Y ELSE
    #marca error en if 
print( "Forma numero 6" )
if n1 >= n2:#if implementan decisiones que implican una o dos alternativas
    if n1 > n2: #Si en una condición se requiere hacer más de una pregunta se puede utilizar un IF anidado.
        print (n1)
    else:#Ejecutan una o varias sentencias de manera condicional
        print(None)
else: #Ejecutan una o varias sentencias de manera condicional
    print(n2)
##USO DE IF Y ELIF Y ELSE
print( "Forma numero 7" )

if n1 <= n2:#if implementan decisiones que implican una o dos alternativas
    if n1 < n2:#Si en una condición se requiere hacer más de una pregunta se puede utilizar un IF anidado.
        print(n2)
    else:#Ejecutan una o varias sentencias de manera condicional
         print(None)
else:#Ejecutan una o varias sentencias de manera condicional
    print(n1)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 8" )

if n1 <= n2:#if implementan decisiones que implican una o dos alternativas
    if n1 == n2:#Si en una condición se requiere hacer más de una pregunta se puede utilizar un IF anidado.
         print(None)
    else:#Ejecutan una o varias sentencias de manera condicional
         print(n2)
else:#Ejecutan una o varias sentencias de manera condicional
    print(n1)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 9" )

if n1 == n2:#lo utilizamos para realizar una comparación entre dos valores y la salida de esta comparación
    print(None)
elif n1 > n2:#se utiliza para comprobar múltiples condiciones si una condición es falsa
     print(n1)
else:#Ejecutan una o varias sentencias de manera condicional
    print(n2)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 10" )

if n1 == n2:#lo utilizamos para realizar una comparación entre dos valores y la salida de esta comparación
    print(None)
elif n1 < n2:#se utiliza para comprobar múltiples condiciones si una condición es falsa
     print(n2)
else:#Ejecutan una o varias sentencias de manera condicional
    print(n1)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 11" )

if n1 == n2:#lo utilizamos para realizar una comparación entre dos valores y la salida de esta comparación
    print(None)
elif n1 >= n2:#se utiliza para comprobar múltiples condiciones si una condición es falsa
    print(n1)
else: #Ejecutan una o varias sentencias de manera condicional
    print(n2)