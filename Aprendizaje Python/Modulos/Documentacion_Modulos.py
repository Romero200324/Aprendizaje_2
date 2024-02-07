
# Importacion de datos de otros proyectos 
import Documentacion_2
print(Documentacion_2.saludo("Oscar")) # Metodo del propio proyecto


# (as) Asignacion de datos a un "Modulo"
import Documentacion_2 as n_hola
n_hola = "Oso".upper()
print(n_hola)

# (from) Para extraer más de una funcion 
from Documentacion_2 import saludo,edad as edad_usuario

# Documento [1]
Saludo_matutino = saludo("Cucho")
print(Saludo_matutino.upper())

# Documento [2]
edad_usuarios = int(input("Dime tu edad : "))

peticion_de_años = edad_usuario(edad_usuarios)
print(peticion_de_años)


# (*) importacion de todos los valores dentro del modulo..

from Documentacion_2 import *

saludos = input("Dime tu nombre: ")
nombre_usuario = saludo(saludos)


edad_usuarios = int(input("Dime tu edad : "))
peticion_de_años = edad_usuario(edad_usuarios)

for i in zip([nombre_usuario],[peticion_de_años]):
    nombres = i[0]
    edades = i[1] 

    print(f"{(nombres)} {(edades)}")

# (__name__) nombre del modulo que importamos 

import Documentacion_2 as Modulo_2

name_modulo = Modulo_2.__name__
print(f"El modulo que importantes fue : {name_modulo}")


