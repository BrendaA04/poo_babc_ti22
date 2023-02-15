"""
    programa4
    Nombre:Brenda ABC
    Fecha: 30/01/2023
    Descripcion:
    CAMBIAR TIPO DE DATO CON int DE OPERACIONES BASICAS 
""" 

numero1 = input("Numero1: ") #solo acepta numeros enteros, bueno solo lee numeros enteros
numero2 = 10 # el valor por el cual se van hacer las operaciones 

suma = int (numero1) + numero2# de acuerdo al numero solicitado  se va a realizar una suma 
print(suma) #va a dar como impresion el resultado de la suma 

multiplicacion = int (numero1) * numero2 #de acuerdo al numero solicitado hace una multiplicacion por el numero establecido 
print(multiplicacion) #imprime el resultado de la multiplicacion 

resta = int (numero1) - numero2 #el numero que ingresa el usuario la va a restar por el numero que esta establecido 
print(resta) #imprime el resultado de la resta 

division = int (numero1) / numero2 #el numero que ingresa el usuario lo divide entre el numero que esta establecido 
print(division) # imprime el resultado de la operacion 

potencia = int (numero1) ** numero2 #el numero ingresado por el usuario lo va a elevar a la potencia del numero establecido 
print(potencia) #imprime el resultado de la operacion 
                #2**10=1024, el resultado seria 1024 y eso es lo que imprime