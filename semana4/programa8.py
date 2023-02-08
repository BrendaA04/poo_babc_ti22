"""
    programa8
    Nombre:Brenda ABC
    Fecha: 07/02/2023
    Descripcion:
    PROGRAMA DE 11 FORMAS DIFERENTES PARA USAR IF
    
"""

n1 = int(input("N1: "))
n2 = int(input("N2: "))
#PROGRAMA DE 11 FORMAS DIFERENTES PARA USAR IF
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1 == n2:
    print(None)

##USO DE IF E IGUAL
print( "Forma numero 2" )

if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
if n2 == n1:
    print(None)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 3" )

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 4" )

if n1 < n2:
    print(n1)
elif n2 < n1:
    print(n1)
else:
    print(None)


##USO DE IF E IGUAL
print( "Forma numero 5" )

if n2 < n1:
    print(n2)
if n1 < n2:
    print(n2)
if n1 == n2:
    print(None)

##USO DE IF Y ELIF Y ELSE
    #marca error en if 
print( "Forma numero 6" )
if n1 >= n2:
    if n1 > n2:
        print (n1)
    else:
        print(None)
else:
    print(n2)
##USO DE IF Y ELIF Y ELSE
print( "Forma numero 7" )

if n1 <= n2:
    if n1 < n2:
        print(n2)
    else:
         print(None)
else:
    print(n1)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 8" )

if n1 <= n2:
    if n1 == n2:
         print(None)
    else:
         print(n2)
else:
    print(n1)

##USO DE IF Y ELIF Y ELSE
print( "Forma numero 9" )

if n1 == n2:
    print(None)
elif n1 > n2:
     print(n1)
else:
    print(n2)

