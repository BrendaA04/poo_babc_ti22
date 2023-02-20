"""
    programaPersona
    Nombre:Brenda ABC
    Fecha: 13/02/2023
    Descripcion:
    Crear una clase alumno para crear objetos con atributos 
    
"""

class Persona:
   def __init__(self):
        __nombre = None
        print("Persona")

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        print("Alumno")

objecto_persona = Persona()
objecto_alumno = Alumno()

objecto_persona.__nombre = "Dejah Thoris"
print(objecto_persona.__nombre)

objecto_alumno.__nombre = "Jhon Carter"
print(objecto_alumno.__nombre)        