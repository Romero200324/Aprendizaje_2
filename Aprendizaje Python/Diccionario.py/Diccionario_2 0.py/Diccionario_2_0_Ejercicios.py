# Ejercicios con todos los valores.

# (dict) Creacion de un diccionario 
creacion_de_diccinario = " (dict) Creacion de diccionario"
print (creacion_de_diccinario.upper())

# 1 Algunos articulos de una tienda }...
print("-------------- Ejercicio 1 --------------")

tienda_martines = dict(Productos_de_limpieza = "Jabon de ropa", Productos_de_cocina= "Cerbilletas", Productos_para_autos = "Llantas")
print(f"En la tienda de matines hay los siguientes articulos {tienda_martines}")


# 2 Crea una lista de platillos para cada cliente 
print("-------------- Ejercicio 2 --------------")

clientes = ["Oscar Romero","Roberto", "Luca", "Roberto 2"]
platillos = ["Pollo Frito","Pan con mantequilla", "Espagrti con albondigas","Adobo de huevo"]
restaurante = ["Palo alto","La sigueña","La de atras","La olla de oro"]

# Añidimiento de Un bucle :

for i in zip(clientes, platillos, restaurante):
    index = i [0]
    valor = i [1] 
    tedor = i [2]
    print(f"El para el cliente {index} recibira el platillo de {valor} y en el restaurante de {tedor}")


# 3 Realiza una lista del mejor promedio 
print("-------------- Ejercicio 3 --------------")

estudiantes_de_ciclo_1 = tuple(["Oscar","Lucas","Roberto","Pagani","Palo","Reni","Lucas","paluca"])
Notas_de_ciclo_final = (3,6,5,6,8,10,5 )

for i in zip(estudiantes_de_ciclo_1, Notas_de_ciclo_final):
    valor_1 = i[0]
    valor_2 = i[1]
    print(f"Los estudiantes fueron calificos y su notas son las siguientes : {valor_1} y su nota es {valor_2}")



# (Frozenset) Congelar los datos para que no se mutan 

#1 Un conjunto de datos de presos que ya casi salen y los que le faltan 

#2 Creacion de un diccionario que contega el registro de entradas y salidas de empleados 

#3 Un lote casas se estan vendien el zona de Mexico con todo sus caracticas 

# (dict.(fromkeys)) creacion de datos / Asignacion de datos 

# 1 Creacion de datos (Empleados que con la cantidad que van haganar)
# 2 Asiga los turnos de trabajo (8 de Agosto del 2023) 
# 3