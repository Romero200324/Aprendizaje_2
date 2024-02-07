#  Todos las operaciones dentro de este modulo : 

# Peticion de valores.
import sys as Localizacion_De_Archivos
Localizacion_De_Archivos.path.append("E:\\python\\Funciones")

from Ejercicios_de_funciones import decuento_de_precios as aplicacion_descuento


# Articulos 
import Listado_de_articulos
def articulos_de_compra ():
    articulos = Listado_de_articulos.lisata_decompreas_del_usuario()
    print(f"Tus articulos son : {articulos}")
#IMPORTACION DE ARCHIVOS 


# HORA

import time
def hora ():
    dia_hoy = time.strftime("%H:%M:%S")
    print(dia_hoy)

# FECHE

import datetime
def fecha ():
    fecha_actual = datetime.date.today()
    print(fecha_actual)






