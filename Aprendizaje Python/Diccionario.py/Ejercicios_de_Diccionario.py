#Ejercios de metodos de diccionario 
#   Diccionario
Base_de_fertilizantes = {  
    
    'Nombre_del_fertilizantes': "Dragón",
    'Compuestos_quimicos_del_producto':["Hibrogeno","Oxigeno","Fosfato"],
    'ubicacion_del_producto':"Mexico",
    'Porcio_recomendada':"5lm",
    'Dias_recomendados':"Del día 6 al día 8",
    'Metodos_de_aplicacion': ["Diluir en agua potable","Evitar el contacto con la piel"],
    'Precuaciones': ["No consumir ningun tipo de alimento durante la aplicación"],
    'Riesgos': ["Espocible que puede contraer un tipo de enfermedad con el tiempo"],
    'Recomendaciones':["Evite el contacto con el producto ya sea en aplicación y un almacen"],
    'Tipo_de_aplicacion':["Deacuerdo a los protocolos de (Salud Ambiental) es recomendable que se aplique en la noche"],
    'Licencias':["Este procducto cuenta con la licencia", "Salud Ambiental", 323234344334, "Salud Ambiental Mexíco"]
}

Base_de_fertilizantes_organicios = {
    'Nombre_del_fertilizantes_organicos':"VegMarina",
    'Compuesto_organico_del_organismo':["Nitrógeno Total", "4%", "Fósforo",	"3%", "Potasio", "1%", "Hierro (Fe)", 216 ,"ppm", "Zinc (Zn)",145 ,"ppm" ,"Cobre (Cu)",	31, "ppm" ,"Manganeso (Mn)"	,3,"ppm", "Boro (B)", 92, "ppm", "Molibdeno (Mo)",1 ,"mg/L","pH",4.24,"CE" ,1.86],
    'Ubicacion_del_fertilizante':"Mexico Puebla",
    'Porciones_recomendadas':"30g",
    'Dias_recomendados_de_aplicacion':"dia 6 al 7 dia",
    'Metodos_de_aplicacion':"Colocarlo antes de una simbra ó preparación de terreno",
    'Precuaciones':"El no correcto del fertilizante(Abonno).No creceran las plantas del tamaño a decuado",
    'Riesgos':"Ahí ferilizantes que si se depositan en un lugar a decuado puede ser dañino para los seres vivos de la zona",
    'Recomendaciones':"La aplicacion adecua debera ser en la madrugada para que la tierra absorba los nutrientes",
    'Tipo_de_aplicacion':"La correcta exparacion por todo el area en donde se piensa sembrar",
    'Dias_de_espera':"Despues de la correcta aplicacion es recomendable esperar la cantidad de 5 a 6 dias habiles",
    'Tipo_del_producto':"La constitiencia de producto es firme y con pedas de comida"

}
# (Keys)  Muestra los nombres de un diccionario
nombres_del_diccionario = "Muestran los indices del diccionario"
print(nombres_del_diccionario.upper())

#1 Busqueda de la liciencias en especificos     
print("------------- Problema 1 ------------- ")

sub_indices_diccionario = Base_de_fertilizantes.keys()
print(f"Estos son los sub indices la base datos de fetilizantes : {sub_indices_diccionario}")

#2 Cuales son los indices de la base de datos de Fertilizantes organicos...
print("------------- Problema 2 ------------- ")

revicion_correcta_de_datos = Base_de_fertilizantes_organicios.keys()
print(f"Los indices de la base de datos son: {revicion_correcta_de_datos}")


#3 Los indices dices de las dos base de datos ( Colectivos)
print("------------- Problema 3 ------------- ")
complemento_de_primer_diccionario = Base_de_fertilizantes.keys()
complemento_de_dos_diccionario = Base_de_fertilizantes_organicios.keys()

print(f"La suma de las dos primeras base de datos son : (1): {complemento_de_primer_diccionario} (2): {complemento_de_dos_diccionario}")

# (get) Busquedas especificas
Busquedas_de_datos = "Datos especificos"
print(Busquedas_de_datos.upper())


#1 En base de datos de fertilizantes (Busca las licciencias del dragón)
print("------------- Problema 1 ------------- ")

Base_de_fertilizantes.get("Liciencias")

print(f"Este producto cuenta con la siguientes liciencias: {Base_de_fertilizantes}")

#2 En la base de datos de fertilizantes organicos (Buscaras los compuestos que contiene el producto)
print("------------- Problema 2 ------------- ")

Base_de_fertilizantes_organicios.get("Compuesto_organico_del_organismo")
print(f"Los compuestos quimicos que contiene son: {Base_de_fertilizantes_organicios}")

#3 En las dos base de datos de los fertilizantes 
# (Buscar el lugar en donde se originan los prodcutos y si son es puebla escribe la direcciones de donde pude comprar)
print("------------- Problema 3 ------------- ")

Recompilacion_de_datos_1 = Base_de_fertilizantes #Mexico
Recompilacion_de_datos_2 = Base_de_fertilizantes_organicios #Puebla

Recompilacion_de_datos_2 = Base_de_fertilizantes_organicios.get("Ubicacion_del_fertilizante")

print(f"El lugar en donde se encuentra es: ({Recompilacion_de_datos_2}) Usted esta cerca del popocateple")

#Union_de_datos_de_diccionario = Recompilacion_de_datos_1 

#if Union_de_datos_de_diccionario == "Puebla":
  #  print("Usted esta ubicado en el volcan de Popocateple")
#else:
 #   print("Lo sienti pero por el momento es posible encontrarte..")



# (pop) Eliminacion de datos especificos
Datos_eliminados = "Elimincion de datos (Especificos)"
print(Datos_eliminados.upper())

#1
print("------------- Problema 1 ------------- ")

#2
print("------------- Problema 2 ------------- ")

#3
print("------------- Problema 3 ------------- ")


# (intens) Agrupacion de datos por separados por conjuntos
Agrupacion_de_conjuntos = "Agrupacion de datos por separaciones"
print(Agrupacion_de_conjuntos.upper())

#1
print("------------- Problema 1 ------------- ")

#2
print("------------- Problema 2 ------------- ")

#3
print("------------- Problema 3 ------------- ")

# (clear) Eliminación de todo el "Array"
Datos_eliminados = "Eliminacion de datos del Array"
print(Datos_eliminados.upper())

#1
print("------------- Problema 1 ------------- ")

#2
print("------------- Problema 2 ------------- ")

#3
print("------------- Problema 3 ------------- ")
