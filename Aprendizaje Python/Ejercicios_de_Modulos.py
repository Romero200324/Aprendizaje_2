# Ejercicio de los modulos 

# (as) Es para la asignacion de nombre a un modulo
print("(as) Es para la asignacion de nombre a un modulo".upper())

# 1 Escojer el nombre de tu mascota perfecto... 
print("""
      ------------------ Ejemplo 1_1 -----------------
      """)

import sys as busqueda
busqueda.path.append("e:\\python\\Modulos")
busqueda.path.append("e:\\python\\Funciones")


import Ejercios_2 as Canes
Canes.nombres_de_canes()

# 2  Hacer un rejor para medir el tiempo en (Horas, Minutos y Segundos).

print("""
      ------------------ Ejemplo 1_2 -----------------
      """)
import Ejercios_2 as hora
hora.hoy()

# 3 Elecion de cancion segun su genero de musica: 

print("""
      ------------------ Ejemplo 1_3 -----------------
      """)

import Ejercios_2 as musica
musica.musica_de_eleccion()

# (from) Para extraer más de una funcion   
print("(from) Para extraer más de una funcion".upper())


# 1 Extracion del archivo de (Ejercicios_de_funciones.py)
print("------------------ Ejemplo 2_1 -----------------")

from Ejercicios_de_funciones import *

# 2 El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
print("------------------ Ejemplo 2_2 -----------------")




# 3
#print("------------------ Ejemplo 2_3 -----------------")


# (*) Importacion de todos los funciones del [modulo]
#print("(*) Importacion de todos los funciones del [modulo]".upper())

# 1
#print("------------------ Ejemplo 3_1 -----------------")

# 2
#print("------------------ Ejemplo 3_2 -----------------")

# 3
#print("------------------ Ejemplo 3_3 -----------------")