# Ejercicios de "Concatenacion con (f)"
#1
print("Sustitucion de (f)".lower)
print ("------------------ Problema 1 ---------------------")
Edad = 20
Validacion_De_Edad = f"Me puedes dicir cuales es tu edad? {Edad} "
print (Validacion_De_Edad)

#2
Mascota = "Perro"
Que_Tipo_De_Mascota = f"Me puedes decir que mascota tienes {Mascota}"
print (Que_Tipo_De_Mascota)

#3
pi = 3.1416
Valor_De_Pi = f"Me puedes dicir cual es el valor de (PI) {pi}"
print (Valor_De_Pi)

# Ejercicio de "Datos compuestos (Array y Tuplas)"

#1 Menú del día
Plato_ligero = "Sopa de tomate"
Plato_fuerte = "Espageti con albondigas"
Acompañamiento = "Pan de trigo"
Postre = "Pay de limón"

Lunes = f"""
            El primer platillo es: {Plato_ligero}
            El segundo platillo sera: {Plato_fuerte}
            El acompañamiento es: {Acompañamiento}
            Y de postre tendremos: {Postre}
            """

Martes = f"""
            El primer platillo es: {Plato_ligero}
            El segundo platillo sera: {Plato_fuerte}
            El acompañamiento es: {Acompañamiento}
            Y de postre tendremos: {Postre}
            """

Miercoles = f"""
            El primer platillo es: {Plato_ligero}
            El segundo platillo sera: {Plato_fuerte}
            El acompañamiento es: {Acompañamiento}
            Y de postre tendremos: {Postre}
            """

Jueves = f"""
            El primer platillo es: {Plato_ligero}
            El segundo platillo sera: {Plato_fuerte}
            El acompañamiento es: {Acompañamiento}
            Y de postre tendremos: {Postre}
            """

Viernes = f"""
            El primer platillo es: {Plato_ligero}
            El segundo platillo sera: {Plato_fuerte}
            El acompañamiento es: {Acompañamiento}
            Y de postre tendremos: {Postre}
            """

semana = [Lunes, Martes, Miercoles, Jueves, Viernes]
print (semana)

#2 Examen de Matematicas
Pregunta_1 = "¿Cuánto es 23 x 24?"
A1 = 23
B1 = 2
C1 = 133

Pregunta_2 = "¿Dime cual es el valor de pi?"

A2= 23.8
B2 = 2.2
C2 = 3.1416

Respuestas_correctas = [C1,C2]
print ( Respuestas_correctas[0])
print (Respuestas_correctas[1])

#3 Pedidos de flores 

Girasoles = 23 
Rosas = 3
Clabeles = 10
Margaritas = 3

Ramo_de_flores = f"""
                Para el ramo de flores cenecesitaran
                Gisalores  {Girasoles}
                Rosas  {Rosas}
                Clabeles {Clabeles}
                Margaritas  {Margaritas}
                """

Listado = [Girasoles, Rosas, Clabeles, Margaritas]

print (Ramo_de_flores) 



#4 Valores de Atomicos de los elementos usando (Tupla)

Oxigeno = 46.40
Silicio = 28.15
Aluminio = 8.23
Sodio = 2.36
Azufre = 0.0260 

Elementos_quimico = (Oxigeno, Silicio, Aluminio, Sodio,Azufre)

Preguntas_de_ciencias = "Cual es el valor Atamico de Alumnio?"


#Ejercicio de Conjunto (Diagrama de BEN)

#1 Un grupo de niños estan en tres equipos diferentes

Alumno_en_equipos = {"Rick","Jose","Sofia","Morty", "Luna","Marte","Pither", "Morty", "Rick", "Rick" }
print(Alumno_en_equipos)

#2
#3


# Ejercicios de Diccionario 

#1 Almacen de producto de ropa
Coopel_ropa_para_niño = {
    'Pantalon_negro' : 10,
    'Camisa_roja': 11,
    'Gorros': 2,
    'Corbatas': 23   
}
print ( Coopel_ropa_para_niño['Gorros'])

#2 Base de datos de (Maiz)
Registro_de_notas = {
    "PH": 7.0,
    "Tipo_de_maiz": "Hibrido",
    "Temperatura": 23,
    "Humedad": "Dry+",
    "Fecha" : "25/07/2023",
}

print(Registro_de_notas["Humedad"])
#
#


# Operadores de comparación 

#1 Comparacion de edades
print ("------------------ Operadores de comparacion 1 ---------------------")
Usuario_edad = 12

if Usuario_edad >= 23:
    print("Usted puede pasar")
else:
    print("Por elemeneto usted no puede pasar")
#2
#3
#4
#5


# Condiciones 

#1 Inicio de sesion 
print ("------------------ Problema 1 ---------------------")
Contraseña_del_usuario = "PolloPicante.2003"
Contraseña_de_la_base_de_datos = "PolloPicante.2003"

if Contraseña_del_usuario == Contraseña_de_la_base_de_datos:
    print ("Contraseña correcta")
else:
    print("Contraseña incorrecta")

#2 Restricion de edades 
print ("------------------ Problema 2 ---------------------")
Edad_del_usuario = 18
Restrincion_de_edades = 19

if Edad_del_usuario <= Restrincion_de_edades:
    print("usted puede pasar")
else:
    print("no pasa")


#3  Ingresos mensuales 
print ("------------------ Problema 3 ---------------------")
ingreso_de_salario = 5000
ingreso_de_mediano = 1500
ingreso_promedio = 2000


if ingreso_de_salario <= ingreso_promedio:
    print("Es un poco pasado del limite de dinero")
elif ingreso_de_salario >= ingreso_de_mediano:
    print("Llgaste al salario de la mitad")
else:
    print("Tu dinero ya casi terminaste")





#4 Medicion de dinero segun tu pais 
print ("------------------ Problema 4 ---------------------")

ingresos_mensuales = 5001
gastos_mesuales = 700

resta =ingresos_mensuales - gastos_mesuales

if ingresos_mensuales > 10000:
    print("Ahora si estas bien")

elif ingresos_mensuales > 5000:
    if ingresos_mensuales - gastos_mesuales <= 5000:
      print(f"No estas bien deja de gastar denero, ya que tienes la cantidad ${resta}")
      print("Es momento de controlar tus deudas")

elif ingresos_mensuales > 30000:
    print("Estarias bien en Venesuela")

else:
    print("Si no tienes dinero es mejor que no hables perro")


