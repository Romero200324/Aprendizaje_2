# Seccion de (Operadores comparación)
Manzanas = 23 == 32
Manzana = 23 != 23

Manzanos = 23 > 34
Manzano = 23 < 23

print (Manzano)

#> Mayor que...
#< Nemor que...



# Condicionales

contreña_del_usuario = "PolloPicante.10"
contreña_de_la_base_de_datos = "PolloPicante.10"

if contreña_del_usuario == contreña_de_la_base_de_datos:
    print ("Contraseña correcta")
else:
    print ("Tu contraseña es incorecta")

# Operadores logicos

#1 AND
Operador = True & True 
Operador = True & False
Operador = False & False

#2 OR
operaciones = True & True 
operaciones = False & True 
operaciones = False & False

#3 NOT
operador = not True 
operador = not False
