# CREACION DE PROGRAMA CON CLASES Y PARA QUE SEA MAS EFICIENTE EN SU PAPEL


import time
import random



class Privacidad ():
    
    #def hoy (self):
     #   self.hora_en_estos_momentos = time.strftime("%H:%M:%S")
      #  print(f"Son las {self.hora_en_estos_momentos}")

    def __init__ (self, password):
        self._password = password

    def propiedad_usuario (self, usuario):
        self,usuario = usuario 


cody = Privacidad ('The passwod is open')
print(cody._password)


# Ejecicio 2  Realizar al usuario ralizar un cambion de password
# Y recordarle cada cuanto debe hacer este cambio..

# Tener una password antes 
# Hacer que esa password cambie por lo que escribio el usuario 
# Y recordar cada cuanto hacer el cambio de password

# class > Codigo mas facil
# Encapsulamiento > Hacer priva la accion


class Usuarios ():

    def __init__(self,usuario1, usuario2,usuario3,usuario4):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.usuario3 = usuario3
        self.usuario4 = usuario4
    

class Passwors (): 
    def __init__(self, password1,password2,password3,password4):
         
         # --> Elementos privado <--
        self._password1 = password1
        self._password2 = password2
        self._password3 = password3
        self._password4 = password4

class Cambio_de_password (Usuarios,Passwors):
    def __init__(self,usuario1, usuario2,usuario3,usuario4, password1,password2,password3,password4):
        


        Usuarios.__init__(self,usuario1, usuario2,usuario3,usuario4)
        Passwors.__init__(self,password1,password2,password3,password4)

        if usuario1 == password1:
            print(f"Bienvenido {usuario1}")
        elif usuario2 == password2:
            print(f"Bienvenido {usuario2}")
        elif usuario3 == password3:
            print(f"Bienvenido {usuario3}")
        elif usuario4 == password4:
            print(f"Bienvendio {usuario4}")
        else:
            print("No ingreso ninguna contraseña...")



conrrecion_de_contraseña = Cambio_de_password("Romero23","PolloPicante","Pezespada","PatoPicante","Romero23","PolloPicante","Pezespada","PatoPicante")
print(conrrecion_de_contraseña._password4)