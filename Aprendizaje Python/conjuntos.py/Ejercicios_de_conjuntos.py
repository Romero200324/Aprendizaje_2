# Ejercicios de (datos de conjuntos)

# (set) Creacion de conjunos
print("Creacion de conjunos".upper())

#1 Crea un conjutos de datos que tengan el mismo valor por cada caso de los datos (Animales terrestres)(Animales de cuatro patas)
print("------------Ejercicios 1---------------") 

Animales_terrestres = set(["Perro", "Serpiente", "Caballo","Mapache","Gusano","Leon"])
Animales_cuatrupedos = set(["Perro","Hipotamo","Gato","Elfante","Caballo","Mapache","Leon"])
union_de_conjutos = (Animales_terrestres, Animales_cuatrupedos)

print(f"""
    El conjunto de datos de (Animales terrestres) : {Animales_terrestres}
    El conujunto de datos de (Animamles cuatrupedos): {Animales_cuatrupedos}
""")
# Unión de ambos conutos : 
print(f"La unión de los datos es: {union_de_conjutos}")



#2 Crea un conjutos de datos de personas que estan en:  (Cada estado aciendo pruedas)
print("------------Ejercicios 2---------------") 


listado_del_personal = ("Alan","Jacinto","Martinez","Andrés","Juan","Nicolás","Antonia","Juana","Noé","Antonio","Juárez","Noelia","Azul","Julia","Paula")
nombres_de_empleados_en_pruebas = set([listado_del_personal])

cuidades_de_Mexico = ("Aguascalientes",
"Baja California",
"Baja California Sur",
"Campeche",
"Chiapas",
"Chihuahua",
"Coahuila",
"Colima")
Lugar_de_recidencias = set([cuidades_de_Mexico])
 # Signacion de datos de a las personas y en donde se en cuentran 

Asignacion_de_cuidades = (nombres_de_empleados_en_pruebas, Lugar_de_recidencias)
print(Asignacion_de_cuidades)




#3 Crea un conjuntos de datos de (Registros de un veterinaria para vacunacion de perros)
print("------------Ejercicios 3---------------") 

vacunas_en_al_macen = ("parvovirus","canino","moquillo","hepatitis","canina","rabia")
Docis_de_aplicaion = set([vacunas_en_al_macen])

perros_de_aplicaon = ("Beagle", "jack", "russell", "terrier", "pastor" ,"alemán", "fox", "terrier", "toy"," yorkshire" ,"terrier", "chihuahua", "pastor alemán", "akita","inu", "labrador","retriever", "bulldog")
Razas_de_perros_de_aplicacion = set([perros_de_aplicaon])

dias_de_vacunacion = set(["Lunes 7 de Agosto del 2023", "Martes 8 de Agosto del 2023", "Miercoles 9 de Agosto del 2023"])

citas_para_perros = (Docis_de_aplicaion, Razas_de_perros_de_aplicacion)
print(f"""Se le indica que habra vacunaciones de a perros, estos dias {dias_de_vacunacion}.
        En donde la vacunas y las razas de los perros seran los siguientes {citas_para_perros}.
        (PARA MÁS IMFORMACION COMUNIQUE SE CON ALGUIEN DEL PLANTEL)
        (Gracias, por su atencion.)
        """)


#(Frocenset) Conservar los datos para que camabien su composicion 


#1 En una un hospital es día de vacunacion y es necesario que todos los paciente del sector (A) reciban las docsis a decuadas las cuales 
# Seran () y para los pasientes del sector (B) las cunas de (). 

# Y todo eso para que al dia siguiente reciban otras vacunas diferentes.


pacientes_del_sector_A = ("Alan","Jacinto","Martinez","Andrés","Juan","Nicolás","Antonia")
pacientes_del_sector_B = ("Juana","Noé","Antonio","Juárez","Noelia","Azul","Julia","Paula")

primer_lote_de_vacunas = ( "Vacuna contra la hepatitis B" ,"Vacuna Hib Vacuna contra el VPH" ,"Vacuna antigripal" ,"Vacuna antimeningocócica")
segundo_lote_de_vacunas = ("BCG","Hep B"	,"Poliomielitis","DTP")


serie_de_vacunacion_1 = frozenset([pacientes_del_sector_A,])
primer_dia_de_aplicacion = { serie_de_vacunacion_1, primer_lote_de_vacunas} 


serie_de_vacunacion_2 = frozenset([pacientes_del_sector_B,])
segundo_dia_de_aplicacion = {serie_de_vacunacion_2, segundo_lote_de_vacunas}


print(f"""
    - Pacienes de la primera docis seran : {pacientes_del_sector_A}
    
    - Los pasientes del segundo lote seran: {pacientes_del_sector_B}

    - Las vacunas son de día 1 : {primer_lote_de_vacunas}  

    - Las vacunas son de día 2 : {segundo_lote_de_vacunas}

    - Y como se muestra en la tabla sera su orden el primer día : {primer_dia_de_aplicacion}

    - Y como se muestra en la tapla sera su orden el segundo día : {segundo_dia_de_aplicacion}
""")

nombre = input("Hola doctor me puede decir su nombre: ")
escriba_contraseña = input("Escriba su contraseña: ")

if escriba_contraseña == "PolloPicante.2003":
    print(f"¡ Bienvenido doctor {nombre}!")
else:
    print("Lo siento esta mal su contraseña ")


Lista_de_aplicacion_dia_uno = {
    'Alan': "Vacuna contra la hepatitis B",
    'Jacinto': "Vacuna Hib Vacuna contra el VPH",
    'Martinez': "Vacuna antigripal",
    'André': "Vacuna antimeningocócica",
    'Juan': "Vacuna contra la hepatitis B",
    'Nicolás': "Vacuna antigripal",
}
Lista_de_aplicacion_dia_dos = { 
    'Antonia': "BCG",
    'Juana': "Hep B",
    'Noé': "Poliomielitis",
    'Antonio': "DTP",
    'Juárez': "BCG",
    'Noelia': "Poliomielitis",
    'Azul': "BCG",
    'Julia': "Hep B",
    'Paula': "DTP"
}
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






reportes_1 = Lista_de_aplicacion_dia_dos.get("Antonia")
reportes_2 = Lista_de_aplicacion_dia_uno.get("Juan")

print(f"""
    Los pacietes del primer aplicacio fueron alergicos a {reportes_1}

    Los pacietes del primer aplicacio fueron alergicos a {reportes_2}
"""
)

Busqueda = input("Indique que paciente quiere buscar :")
Busqueda_elementos = Datos_masivos.get(Busqueda)
print(Busqueda_elementos)

Busqueda = input("Indique que paciente quiere buscar :")
Busqueda_elementos_2 = Datos_masivos.get(Busqueda)
print(Busqueda_elementos_2)

#2 Crea un conjunto para un banco : En un bacano les dara un bonus a unos clienrtes que cumplan con condiciones
#Las cuaales seran : 
# Y podran recibir un credito de ($1000)

clinte_Perfil_del_cliente = {
    'Antonia': 2000,
    'Juana': 3000,
    'Noé': 500,
    'Antonio': 3000,
    'Juárez': 1000,
    'Noelia': 7000,
    'Azul': 4389,
    'Julia': 463,
    'Paula': 343,
}


Busqueda_de_clientes = input("Ingrese un nombre para saber si puede tener el bonus: ")
Nombre= clinte_Perfil_del_cliente.get(Busqueda_de_clientes)

if Nombre >= 5000:
    print("Filicidades usted es acredor a tener el bonus:")
else:
    print("Lo siento pero no padra ser acredor por que usted solo tiene menos de 5000")


#3 En una Universidad para entrar tienes que decir tu ID :
# Pero hay dos grupos los que pagaron y los que no indica cual si pagaron y cuales no ...


Estudiantes = {
 'Antonia': 2000,
    'Juana': 3000,
    'Noé': 500,
    'Antonio': 3000,
    'Juárez': 1000,
    'Noelia': 7000,
    'Oscar': 177020
}

Estudiantes_no_pasan = 11223,31222,12333,44455,53332

Dime_tu_Id = input("Ingresa tu ID: ")
Busqueda_estudiantil = Estudiantes.get("Dime_tu_Id")

if Busqueda_estudiantil == 11223:
    print("Estatus no pagado")

else:
    print("Estatus pagado 😉")


# Ejercicios de 


