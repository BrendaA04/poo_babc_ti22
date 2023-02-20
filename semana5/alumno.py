"""
    alumno.py
    Nombre:Brenda ABC
    Fecha: 13/02/2023
    Descripcion:
    Crear una clase alumno para crear objetos con atributos 
    
"""
class Alumno: #crea una clase 
    __nombre = None #se declara __nombre como una variable privada con un valor None 
    __matricula = None #se declara __matricula como una variable privada con un valor None 
    __carrera = None #se declara __carrera como una variable privada con un valor None
    
    def __init__(self): #funcion que inicia la clase 
        print("Alumno") #va a imprimir el texto alumno

    def setNombre(self,nombre): #funcion que asigna valor a la variable nombre 
        self.__nombre = nombre #el valor de __nombre sera igual a nombre 

    def getNombre(self): #funcion que asigna valor a la variable nombre 
        return self.__nombre #va a retornar el valor __nombre

    def setMatricula(self,matricula): #funcion que asigna valor a la variable matricula 
        self.__matricula = matricula #el valor de __matricula sera igual a matricula 

    def getMatricula(self): #funcion que asigna valor a la variable matricula 
        return self.__matricula #retorna el valor de la __matricula

    def setCarrera(self,carrera): #funcion que le asigna un valor a la variable carrera
        self.__carrera = carrera # el valor de carrera sera igual a carrera 

    def getCarrera(self): #funcion que le da valor a la variable carrera 
        return self.__carrera #retorna el valor de  __carrera

brenda = Alumno() #crea un objeto de la clase alumno
brenda.setNombre("Brenda") #usa setNombre para asignarle al objeto un nombre
print(brenda.getNombre()) #va a imprimir la funcion getNombre esto es para mostrar el nombre

brenda.setMatricula("1722110244") #esa setMatricula para asignarle una matricula al objeto 
print(brenda.getMatricula()) #va a imprimir la funcion getMatricula esto es para mostrar la matricula 

brenda.setCarrera("Hacer un software") #usa el setCarrera para asignarle al objeto una carrera 
print(brenda.getCarrera()) #imprime la funcion getNombre para mostrar la carrera 