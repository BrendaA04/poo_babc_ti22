from persona  import Persona #importa la clase persona que se encuentra en el archivo persona.py

class alumno (Persona): # crea la clase alumno que se esta heredando de la clase persona
    def __init__(self) -> None: #contruye la clase alumno
        super().__init__() #llama al constructor de la clase persona
        print("Alumno") #imprime el texto alumno 

objeto_alumno = alumno() #creara un objeto de la clase alumno



