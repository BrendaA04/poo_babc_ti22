"""
    profesor.py
    Nombre:Brenda ABC
    Fecha: 13/02/2023
    Descripcion:
    Importa la clse persona del archovo persona.py y se crea la clase profesor que hereda de la clase persona, llamando a un contructor de clase persona 

    
"""

from persona import Persona #importa la clse persona del archovo persona.py

class profesor (Persona):#crea la clase profesor que hereda de la clase persona
 
 def __init__(self)-> None: #constructor de la clase profesor
    super().__init__() #llama al constructor de la clase persona
    print("Profesor") #imprime el texto profesor 

objeto_profesor = profesor() # crea un objeto de la clase profesor