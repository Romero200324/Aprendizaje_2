#dir (Los atributos que podrian tener...)

#1  
#2
#3
#4

# type (El tipo de dato que saria...)
tipo_de_dato = "type"
print(tipo_de_dato.upper())

#1 Para el siguiente caso me pudes decir cual es el tipo de dato 
print("----------- Ejercicio 1 -----------")
valor_inpuesto = int(input("Me puede dar un numero: "))
operaciones_de_secciones = 23 * valor_inpuesto
valor_final = type(operaciones_de_secciones) 

print(f"Resultado y tio de datos es:  ({valor_final})")


#2 Cual es el tipo de dato no daba la operaciones
print("----------- Ejercicio 2 -----------")

numero_de_peticion = int(input("Paticion de numeros: ")) # Saber que tipo de dato es ..
operaciones_en_proceso = 32 + 33 + 34 * numero_de_peticion
type(operaciones_en_proceso)

if operaciones_en_proceso >= 342:
    print(f"Lo siento pero el dato es mucho: {operaciones_en_proceso}")
else:
    print(f"El dato no es superio ya que el valor de dato es :{operaciones_en_proceso}")

#3 Declaracion de datos...
print("----------- Ejercicio 3 -----------")

valor_inmutable = tuple(["Nombre", "Oscar","Primer_Apellido","Romero","Segundo_Apellido","Romero"])
resultado_de_valor = type(valor_inmutable)

print(f"El tipo de dato que esta compuesto es: ({resultado_de_valor})")



#upper (Letras mayusculas)

#1 Escribe tu CURP
curp_en_el_servidor = "RORO030613HPLMMSA7" #roro030613hplmmsa7
servidor_copleaños = 2003

Campo_en_rellenar = "roro030613hplmmsa7"
año_de_compleaños = 2003

if año_de_compleaños == servidor_copleaños:
    minusculas = curp_en_el_servidor.lower()
    if curp_en_el_servidor and Campo_en_rellenar == minusculas: 
        print("""
            Tu curp esta mal, pero es muy paracido pero en algo esta mal... \n
            Pero deja te corrijo tu error, \n
            Listo : """ + Campo_en_rellenar.upper()) 
else:
    print("Nose pudo intenta otra vez...")


#2 En documentos de tramites
escritura = "oscar romero romero"
Documento = escritura.upper()

if escritura == Documento:
    print(f"Tu papel fue recibido, gracias {Documento}")
else: 
    print(f"por favor escriba bien su nobre {escritura}")

#3
#4

#lower (letras minusculas)

#1 Para concursar en una entrevista escribe tu nombre mimusculas 
nombre_del_participante = "ROMERO ROMERO OSCAR"
if nombre_del_participante == nombre_del_participante.lower():
    print("Tu nombre no esta bien escrito por favor corijalo")

elif nombre_del_participante == nombre_del_participante.upper():
    print("Mal pero pues ya que lo voy a correjir \n")
    cambio_de_nombre = nombre_del_participante.upper()
    print(cambio_de_nombre.lower())


else:
    print("Por elmoneto es puedo dejarte pasar por errores..")

#2
#3
#4

#capitalize (Corrije el texto y coloca la primera letra en mayuscula)

#1 Titulo de cartel 
nombre_del_cartel = "Bienvenido AL CUSEO DE MATEMATICAS"

correciones_de_errores = nombre_del_participante.capitalize()
print(correciones_de_errores)

#2 codiar texto en mayuculas
texto = "habia una vez un pez que volava pero nunca puedo APRENDER A CAMINAR POR QUE UN DÍA SE LO COMIO UN GATO..."
parametro_de_texto = texto.capitalize()
print(parametro_de_texto)

#3
#4

# Busqueda de palabras en el codigo...
Lista_de_contactos = """
                    oscar romero romero 
                    pedro romero romero 
                    erasmos romero romero 
                    heidy carreto romero
                    abelina romero valencia
                    pedro romero arias
                    elizathe romero romero
                    carlos romero romero 
                    """
Busqueda_de_contactos = Lista_de_contactos.find("romero romero")
print(Busqueda_de_contactos)

# index "Detencion de programas por ECEPCIONES"

#1 si la temperatura es mayor a un cieto valor cierra la puerta
temperatura = 34
temperatura_fria = 199
temperatura_maxima = 1000
temperatura_estable = 5000
emergencia= "Peligro"
peligro = "Corre"
valor = temperatura + temperatura_maxima

if temperatura + temperatura_fria == temperatura_estable:
    print(f"Todo esta bien la temperatura es : {temperatura}")

elif temperatura - temperatura_maxima == temperatura_estable:
    print(f"Es un poco pelegriso ya que la temperatura es: {temperatura}")

elif temperatura_estable + temperatura_maxima == temperatura_fria:
    resultado = emergencia.replace("Peligro","Se le endica que todo el personal debera de salir por su bien")
    print(resultado)

elif  valor >= temperatura_fria:
    alta_tencion = peligro.index("r")
    print(alta_tencion)

else:
    print("Llama a los bomberos el número es: 911")


# Metodos de listado
titulo = "Metodos de listado"
print(titulo.upper())

#len

#1 Para saber cuantos elemetos tiene la base de datos (Fertilizantes)
print("------------- Problema 1 -------------")

base_de_datos_fertilizantes = (["Canidad_de_porcion", 23, "Metodo_de_aplicacion","Noche",18.00])
print(len(base_de_datos_fertilizantes))

#2 Lista de productos en una papeleria
print("------------- Problema 2 -------------")

papeleria = list(["papel","goma","lapiz","Sacapuntas","libretas","silicon","pegamento"])
conteo_de_productos = len(papeleria)

print(f"Cuantos articulos entemos disponibles..? Cantidad {conteo_de_productos}")

#3 Cuantos alumnos hay en el salon 3A y 5B
print("------------- Problema 3 -------------")

grupo_3A = list(["Oscar","Alberto","Ben"])
grupo_5B = list(["Blue","Bingo","Chili","Bandid"])

conjuntoA = (len(grupo_3A))
conjuntoB = (len(grupo_5B))

print(conjuntoA)
print(conjuntoB)

#append () Agregar datos nueveos a una Array
Agregacion_de_datos = "append"
print(Agregacion_de_datos.upper())

#1 Lista de emplados que cumplen años el 29/07/2023
print("------------- Problema 1 -------------")
empleados_del_area_de_ventas = list(["Oscar","Roberto","Alverto","Lucas"])
mes_de_cumple_años = "29/07/2023"

empleados_del_area_de_ventas.append("Jack") # Recuerda solo un elemento 

print(f"El día de hoy {mes_de_cumple_años} se celebran a las personas por cumplir años en esta empresa {empleados_del_area_de_ventas}")


#2 Gastos de una persona (Agregando un gasto del utimo día)
print("------------- Problema 2 -------------")

gastos_del_dia = list(["Dona","cafe","Tamal de mole","Tacos de pastor","cafe","samwich"])
cierre_del_día = "30/07/2023"

gastos_del_dia.append("Multa por estacionarse en donde no devia")

print(f"El registro de gatos del día {cierre_del_día} los cuales fuerón {gastos_del_dia}")

#3 Lista de compras en súper mercado 
print("------------- Problema 3 -------------")

Lista_de_compras = list(["Huevo","Cafe","Leche","Jamón","lechuga","Jalápeños"])
Lista_de_compras.append( "Papel de baño")

print(f"Las compras de esta semana es de :  {Lista_de_compras}" )

#insert (Colocar un nuevo elemento en una posicion fija en el Array)
posicion_fija = "inset"
print(posicion_fija.upper())

#1 Lista de fecha de cumple años sera : Día / Mes / Año
print("------------- Problema 1 -------------")

composicion_de_fecha_de_cumpleaños = list(["Día",",Mes","Año"])
sector_de_diseño = "empleado_1"

sector_de_diseño = list(["NOMBRE", "oscar","DIA","13","MES","AÑO",])

sector_de_diseño.insert(5,"06")
sector_de_diseño.insert(7,"2003")

print(f"""
    Corección de fecha de cumpleaños de los empleados seguira la siguiente estructura.\n
    Para la correcta estructuración de datos{composicion_de_fecha_de_cumpleaños} el primer empleado sera \n
    {sector_de_diseño}.
    """)



#2  Asignaciones de tareas por hacer el dia de 30/07/2023
print("------------- Problema 2 -------------")

tareas = list(["Ir por las compras","Cocinar para La cena","Dormir al menos 5 horas al día"])
tareas.insert(3,"Ir por el perro al paque")

nombres = "Oscar" 
dias = "Lunes"

print(f" Iniciamos con {nombres} para que haga las tareas del día {dias} con {tareas} ")


#3  Dianostico para resolver problemas tales como...
print("------------- Problema 3 -------------")

procedimiento_para_problemas = {
    'Paso 1' : "Detectar el problema ",
    'Paso 2' : "Saber como arreglar el problema ",
    'Paso 3' : "Usar las herramientas a decuadas para la correcion",
    'Paso 4' : "Si el problema es grande llama por ayuda ",
    'Paso 5' : "!PERRA HARA EXPLOCION¡"
}

llamada = "Paso 6 : fue"
pasos_de_emerjencia = list(["Paso 7" ])


paso_6 = llamada.replace("fue", "El número de emergencia es 911")
pasos_de_emerjencia.insert(1,"Llego la ambulancia estmaos salvados")

print(f"El procedimiento para arreglar una Bomba Atomica es : {procedimiento_para_problemas} {paso_6} {pasos_de_emerjencia}")



#extend () Agregar un Array en otro Array 
array_a_array = "extend"
print(array_a_array.upper())

#1 Nombres de emplados y cantidad de paga
print("------------- Problema 1 -------------")

Nombres_del_sector_A = list(["Oscar","Roberto","Jack","Luca","Portoroso"])
Sueldo = list(["$23.0000","$2300","$10000","$120000","$213,33"])

Nombres_del_sector_A.extend([Sueldo])
print(f"El suedo esta asi en esta cantidades de {Nombres_del_sector_A}")

# 2 Día de pedidos por llegr y de que provedor sera
print("------------- Problema 2 -------------")

entregas_de_la_samana = list([ "Lunes: 30/07/2023","Martes: 31/07/2023","Miercoles: 1/08/2023","Jueves: 2/08/2023","Viernes: 3/08/2023"])
provedores = list(["Bingo", "Sabritas","Alpura","Chimex","Fut"])

entregas_de_la_samana.extend(provedores)
print(f"Los pedidos de la proxima semana seran {entregas_de_la_samana}")

#3 Ventas de casas y dueños de la propietarios
print("------------- Problema 3 -------------")

clientes = list(["Oscar Romero", "Luca Pagari","Alberto Pagari","Roberto Porcendente"])
zona_de_la_propiedad = tuple(["Puebla","Mexico","Estados Unidos","Puebla Las Lomas","España"])


clientes.extend(zona_de_la_propiedad)
print(f"Estos son los propitarios de sus casas son : {clientes} ! Gracias por su compra ¡")


# (pop) Eliminacion de un elemnto de una lista
eliminacion_de_listado = "Eliminacion de un elemento de una lista"
print(eliminacion_de_listado.upper())


#1 Empleados que ya no trabajan aquí
print("------------- Problema 1 -------------")

lista_de_empleados = list(["Oscar","Lucas","Romero","Ricado","Pollo","Picante","Pedro","Oscatr"])
lista_de_empleados.pop(4)

print(f"Los empleados de esta lista ya no estan en la empresa {lista_de_empleados}")



#2 Limpieza de datos "Borrar datos (Vacios)"
print("------------- Problema 2 ------------- ")

base_de_datos_empleados = ("Oscar Romero Romero Carlos Alan Jacinto Martinez Andrés Juan Nicolás f f f f f f f Antonia Juana Noé Antonio Juárez Noelia Azul Julia Paula")
separacion_de_datos = base_de_datos_empleados.replace("f"," Romero")

datos_en__un_array = separacion_de_datos.split(" ")

datos_en__un_array.pop(2)

print(f"Paso 3 : {separacion_de_datos}")


#3 Liempieza de datos (Borrar datos duplicados).
print("------------- Problema 3 ------------- ")

Base_de_datos_numerica = {2,3,455,66,444,33,234,675,56,23,45.,432,3,455,66,444,33,234,675,56,23,45,43,"d","d","d","d","d","d" }

print(f"Los datos estan limpios para ejecutar el paso seguiente : {Base_de_datos_numerica}")





# (sr)  Nombrar el elemento que vamos a eliminar
sr_elemento_de_array = "Nombrar el elemento que vamos a eliminar"
print(sr_elemento_de_array.upper())


#1 Busqueda de datos basios para eliminarlos
print("------------- Problema 1 ------------- ")

datos_repitidos = list(["Lapíz","Papel","Carton","Tijeras","Tijeras","Pollo","Donas","Cafe","Recistol","Goma"])
datos_repitidos.remove("Pollo")

print(datos_repitidos)

#2 Cambiar el nombre en todo los documentos..
print("------------- Problema 2 ------------- ")


Papeles_importantes = list(["oscat","oscat","Oscar Romero Romero"])


Papeles_importantes.remove("oscat")

if Papeles_importantes != "oscart":
    print("Datos eliminados")
else:
    print("No se contraron datos similares")


#3 Cambio de fecha de la cita en una entrevistas.
print("------------- Problema 3 ------------- ")


# (clear) Eliminar todo el Array 
eliminacion_de_array = "Eliminar todo el Array "
print(eliminacion_de_array.upper())


#1 Eliminacion de la base de datos de (Formacion_de_tierras)
print("------------- Problema 1 ------------- ")

#2 Registro de base de datos para la base de datos
print("------------- Problema 2 ------------- ")

#3 Si dos Array son iguales elimina el elmento
print("------------- Problema 3 ------------- ")


# (sort) Formar de forma accedente 
accedente = "De forma accedente"
print(accedente.upper())


#1 Cual es el promedio del Alumno más alto
print("------------- Problema 1 ------------- ")

#2 Cual es el sueldo más barrato y con más horas
print("------------- Problema 2 ------------- ")

#3 Las multiplicaciones y el resultado de menor al mayor
print("------------- Problema 3 ------------- ")


# (sort.(reversed = True)) Forma de desedente
Desedente = "Forma de desedente"
print(Desedente.upper())


#1 Cual fue el promedio mas bajo de los alumnos
print("------------- Problema 1 ------------- ")

#2 Cual es el precio mas bajo del mercado de las verduderias
print("------------- Problema 2 ------------- ")

#3 Cual es el precio mas bajo de la bolsa de valores (Y en el momento mas bajo "Se le informara de que es momento de vender o comprar") 
print("------------- Problema 3 ------------- ")

# reverse (Le da la vuelta completa a todo tipo de "Listado")
vuelta = "Le da vuelta completa a un Array"
print(vuelta.upper())

#1 Listado de alumnos con mayor promedio a los peores 
print("------------- Problema 1 ------------- ")

#2 Inventario de una teineda (El ultimo articulo de la posion)
print("------------- Problema 2 ------------- ")

#3 Lista de compras del súper mercado...
print("------------- Problema 3 ------------- ")