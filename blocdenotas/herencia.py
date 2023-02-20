"""
    programaPersona
    Nombre:Brenda ABC
    Fecha: 14/02/2023
    Descripcion:
    Crear una clase  persona y una clase de alumno que hereda los atributos y metodos de la clase persona  
    
"""

class Persona: #crea una clase persona 
   def __init__(self): #contructor de la clase persona 
        __nombre = None #crea una variable privada __nombre 
        print("Persona")#imprime como texto Persona 

class Alumno(Persona): #crea la clase alumno que hereda la clase persona 
    def __init__(self): #constructor de la clase alumno
        super().__init__() #aqui llama al constructor de la clase persona 
        print("Alumno")# va aimprimir el texto persona 

objecto_persona = Persona() #crea un objeto de la clase persona 
objecto_alumno = Alumno() #crea un objecto de la clase alumno 

objecto_persona.__nombre = "Dejah Thoris" #Aqui asigna valor en la variable __nombre para el objeto persona 
print(objecto_persona.__nombre) #imprime el valor en nombre 

objecto_alumno.__nombre = "Jhon Carter" #Aqui se asigna un valor a la variable __nombre para el objeto __alumno
print(objecto_alumno.__nombre)  #imprime el valor en __nombre  