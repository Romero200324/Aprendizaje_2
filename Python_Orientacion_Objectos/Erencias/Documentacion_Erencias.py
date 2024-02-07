# En esta parte estara todo sobre herencias en clases de python
class Personas :
    def __init__ (self,nombre,edad,Nacionalidad,peso,estatura):
        self.nombre = nombre
        self.edad = edad
        self.Nacionalidad = Nacionalidad
        self.peso = peso
        self.estatura = estatura


    def hablar(self):
        print("Hola,como estas")



# Herencias de clases... 
class Empleado(Personas):

    #(pass) Dato no definido y este dato basio
    #----- pass --------- 
    def __init__(self,nombre,edad,Nacionalidad,peso,estatura,trabajo,salario):
        # (super) Que dato va heredar de las funciones de la clase pabre
        super(). __init__(nombre,edad,Nacionalidad,peso,estatura)
        self.trabajo = trabajo
        self.salario = salario

   # Herencia simple 
    def hablar(self):
        print("Holo, ya tevas adios...") 

class Estudiante(Personas): 
    def __init__(self,nombre,edad,Nacionalidad,peso,estatura,Homowork,Clases):
        super().__init__(nombre,edad,Nacionalidad,peso,estatura,)
        self.tarea = Homowork
        self.clases = Clases


estudiante = Estudiante("oscar Romero",20,"Mexicana",58.5,1.70,"Programacion Orienta a Ojectos",13)
print(estudiante.tarea)

myname = Empleado("Oscar",20,"Mexicana",58.5,1.70,"Programacion",13433)
myname.hablar()