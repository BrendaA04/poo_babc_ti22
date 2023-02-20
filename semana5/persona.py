"""
    persona.py
    Nombre:Brenda ABC
    Fecha: 13/02/2023
    Descripcion:
    Crear una clase persona para crear dos variables o atributos que obtendran valor con la funcion set y lo devolvera la funcion get 
    
"""


class Persona: #crea la clase persona 
    __nombre = None #declara como privada la variable __nombre con valor None 
    __email = None #declara como privada la variable __email con valor None 

    def __init__(self): #esta funcion inicia la clase 
        print("Persona") #va a imprimir el texto Persona 

    def setNombre(self,nombre): #funcion que asigna valora a la variable nombre 
        self.__nombre = nombre #el valor de __nombre sera igual a nombre 

    def getNombre(self): #funcion que obtiene  valor a la variable nombre 
        return self.__nombre #retorna el valor de nombre 

    def setEmail(self,email): #funcion que asigna valor a la varible email
        self.__email = email  #el valor de variable __email sera igual a email

    def getEmail(self): #funcion que obtiene el valor de la variable email
        return self.__email #retorna el valor de la variable email 

dejah = Persona() #crea un objeto de la clase persona 
dejah.setNombre("Dejah") #setNombre para asignar un nombre al objeto 
print(dejah.getNombre()) #imprime la funcion getNombre para imprimir el nombre 
dejah.setEmail("correo@gmail.com") #setEmail para asignar un correo o email al objeto 
print(dejah.getEmail()) #imprime la funcion getEmail para imprimir el email 
