# Ejercicios sobre los metodos en orientacion a objectos...

class registro_perruno:
    def __init__(self,perro):
        self.nombrar = perro

    # Metodo es esto:
    def nombre_raros ():
        import random as rm 
        numeros_random = rm.randrange(0, 5)

        if numeros_random == 1:
            print("Orejas largas")
        elif numeros_random == 2:
            print("Mocho de cola")
        elif numeros_random == 3:
            print("Loco por los cocos")
        elif numeros_random == 4:
            print("Coco gueco")
        else:
            print("Mole")
        
registro_perruno.nombre_raros()
  
#   EJERCICIO DE ALUMNOS CON PETICION DE SU NOMBRE Y SU EDAD PARA DARLE MATERIAS A LAS CUALE ESTA ESCRITAS 

class Alumnos:
 def __init__(self,Nombre,edad,Materias,Horario,Turnos,id_alumno):
    self.numero_de_materias = Materias
    self.Inicio_de_clases = Horario
    self.Turno = Turnos
    self.nombre_del_alumno = Nombre
    self.edad_del_alumno = edad
    self.id_alumno = id_alumno

# Peticion de datos al usurio 
Peticion_de_nombre = input("Ingres su nombre para saber sus materias: ")
Peticion_de_id = input("Ingrese su id para saber tu matirias: ")
edad_del_alumno = input("Coloque su edad para saber su maetirias: ")


alumno_0 = Alumnos(Peticion_de_nombre,int(edad_del_alumno),"\nSpanis\n Matematicas \n Ingles \n Historia \n Calculo 1 \n Matematicas para pensar","23:23 am","Matutino",int(Peticion_de_id))
print(f"Sus materias son: {alumno_0.numero_de_materias}")
