# Estos seran los ejercicios con bucles

# (list) Combinacion con una lista 

# 1  # Ejercicio de "Datos compuestos (Array y Tuplas)"

#1 Menú del día
dias_de_la_semana = tuple(["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])
platillos = ["Sopa de tomate","Pan de trigo","Espageti con albondigas","Pay de limón","Helado de chocolate","Platanos con crema","Helado de vanilla"]
secuencia = ["primer","segundo","tercero","cuarto","quinto","sexto","septimo"]

for i in zip (dias_de_la_semana,platillos,secuencia):
    valor_1 = i [0]
    valor_2 = i [1]
    valor_3 = i [2]

    print (f" El dia {valor_1} el {valor_3} platillo sera: {valor_2}")

# 2 Python en cada uno de sus letras 
palabra = "Python"

def valort ():
    for i in palabra:
        valor_5 = i [0] 
    
    if i == str(6):
        print("Valido")


    
    print(valor_5)


  
# 3 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


peticion_de_datos = input("Me puede decir 10 animales para una lista: ")

for i in enumerate([peticion_de_datos ]):
    index = i [0]
    cantida = i [1]
    print(f"El nuemero de palabra es {index} y tu palabra es {peticion_de_datos}")



# 4 Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


edad = int(input("Dime cuantos años tienes: "))

for años in range(1,edad+1):
    print(f"Los años que vas vivo son : {años}")

if edad == 20:
    print(f"Feliz cumpleaños {edad}")
elif edad == 19: 
    print(f"Ya casi eats cerca {edad}")
elif edad > 21:
    print(f"Usted ya esta un poco pasado {edad}")
else:   
    print("Uy todavia falta muhco...")
# 10 en 10 


# (zip) Para unir mas de dos listas 

#1 Hacer un  arbol de navidad 
estrellas = "Arbol de " 
lineas = "navidad" 
for i in zip([estrellas],[lineas]):
    decoracion_1 = i[0]
    decoracion_2 = i[1]
    print (f"El {decoracion_1}{decoracion_2}")


#2 Barajar combinacion de  cartas de dos tipos de cartas

barajas_de_primer_monto = ["Reina","Corona","Naipes","As de espada","As de corazon","Reina de corazones","Trebol"]
barajas_de_segundo_monto = [1,2,3,4,5,6,7,]

for i in zip(barajas_de_primer_monto, barajas_de_segundo_monto):
    linea_1 = i [0]
    linea_2 = i [0]
    print(f"Monto de barrjas quedara de la siguiente manera {linea_1} y {linea_2}")




#3 Estatura y pesos de pacinetes del hospital
 
estaturas = [1.5,14.5,45.7,23.4]
pesos = [23,26,44,11,33,66]
nombres_de_pacientes = ["Oscar","Hugo","Romero","Luca"]

for i in zip(estaturas,pesos,nombres_de_pacientes):
    nota_1 = i[0]
    nota_2 = i[1]
    nota_3 = i[2]
    print (f"El paciente {nota_3} tiene el peso de {nota_2} kg y de altura es {nota_1}m")


# (rango) Para indicar el rengo del bucle



#1 En una un hospital es día de vacunacion y es necesario que todos los paciente del sector (A) reciban las docsis a decuadas las cuales 
# Seran () y para los pasientes del sector (B) las cunas de (). 

# Y todo eso para que al dia siguiente reciban otras vacunas diferentes.


pacientes_del_sector_A = ["Alan","Jacinto","Martinez","Andrés","Juan","Nicolás","Antonia"]
pacientes_del_sector_B = ["Juana","Noé","Antonio","Juárez","Noelia","Azul","Julia","Paula"]

primer_lote_de_vacunas = [ "Vacuna contra la hepatitis B" ,"Vacuna Hib Vacuna contra el VPH" ,"Vacuna antigripal" ,"Vacuna antimeningocócica"]
segundo_lote_de_vacunas = ["BCG","Hep B","Poliomielitis","DTP"]


for i in zip(pacientes_del_sector_A,primer_lote_de_vacunas):
    pacientes_1 = i[0]
    lote_1 = i[1]
    print("El primer dia de vacunascion seroan para los siguinetes:")
    print(f"Paciente {pacientes_1} y la vacuna sera : {lote_1}")

for i in zip(pacientes_del_sector_B,segundo_lote_de_vacunas):
    pacientes_2 = i[0]
    lote_2 = i[1]
    print("El segundo dia de vacunascion seroan para los siguinetes:")
    print(f"Paciente {pacientes_2} y la vacuna sera : {lote_2}")


# 2 Enumera las razas de perros 

# 3 Enumera enumera unas lista

# (enumerate) un conteo de veces que se ejecutan 


# (else) Al tenminar del bucle imprime un resultado

#1 
#2
#3

# (.items) Para leer el contenido de un diccionario 

#1 
Datos_masivos = {
    'Antonia': "BCG",
    'Juana': "Hep B",
    'Noé': "Poliomielitis",
    'Antonio': "DTP",
    'Juárez': "BCG",
    'Noelia': "Poliomielitis",
    'Azul': "BCG",
    'Julia': "Hep B",
    'Paula': "DTP",
    'Alan': "Vacuna contra la hepatitis B",
    'Jacinto': "Vacuna Hib Vacuna contra el VPH",
    'Martinez': "Vacuna antigripal",
    'André': "Vacuna antimeningocócica",
    'Juan': "Vacuna contra la hepatitis B",
    'Nicolás': "Vacuna antigripal",
}

for i in Datos_masivos.items():
    print(f"los valores : {i}")
#2
#3

# (continue) Para saltar un dato que no queramos 
#1
# 2
# 3

# (breack)

#1
#2
#3

# (for) En una sala cadena de codigo.

#1 Tienda de valores 

tienda = ["Sopa","Pan","Paletas","Cereal","Chocolate","Leche","Huevo"]
compras = [x for x in tienda]
print(f"Copras: {compras}")


#3
