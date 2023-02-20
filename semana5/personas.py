"""
    personas.py
    Nombre:Brenda ABC
    Fecha: 13/02/2023
    Descripcion:
    Crear una clase llamada persona que se convertira en la clase padre de la clase alumno, prfesor, coordinador 
    
"""

class Persona: #crea la clase persona 
    def __init__(self) -> None: #contructor de la clase persona
        print("Persona") #imprime el texto persona 

class Alumno(Persona): #crea la clase Alumno que se hereda de la clase Persona 
    def __init__(sel) -> None: #contructor de la clase Alumno 
        super().__init__()#llama al constructor de la clase persona
        print("Alumno") #imprime el texto Alumno 

objeto_alumno = Alumno() #crea un objeto de la clase Alumno 

class Profesor(Persona):#crea la clase profesor que se hereda de la clase persona 
    def __init__(self) -> None: #constructor de la clase profesor 
        super().__init__() #llama al constructor de la clase persona 
        print("Profesor")#imprime el texto profesor 

objeto_profesor = Profesor() #crea un objeto de la clase profesor 

class Coordinador(Persona): #crea la clase coodinador que se hereda de la clase persona 
    def __init__(self) -> None: #constructor de la clase coordinador 
        super().__init__() #aqui llama al constructor de la clase persona 
        print("Coordinador") #imprime el texto que dice coordinador 

objeto_profesor = Coordinador() #crea un objeto de la clase de coordinador 

    
        

    