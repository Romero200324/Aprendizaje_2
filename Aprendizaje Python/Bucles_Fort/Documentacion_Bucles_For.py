# Documentacio de Bucles en diferentes tipo de Array

#(List) incio de Bucles
animales = ["Perro","Faca","Gallina","Gato"]
objectos = ["Silla","Lapiz","Goma","Pc"]
enumeracion = [23,232,12,335,6]

for animal in animales:
    print(f"La variable tedra los valores de : {animal}")

for objecto in objectos:
    print(f"Listado los objectos es : {objecto}")


# (zip) Para la unión de dos listas
for animal,objecto in zip(animales,objectos):
    print(f"Para el listado 1 es : {animal}")
    print(f"Para el listado 2 es : {objecto}")

# (rango) Para indicar el rango de bucle
for num in range(20,41):
    print(f"El listado es igual a : {num}")

# Otra forma que tambien se puede definir de la siguientes forma
for numer in range(12):
    print(f"La numeracion es de la forma: {numer}")

# (enumerate) Para numerar unalista 
for recorido in enumerate(enumeracion):
    print(recorido)

# Otra forma para imprimir 

for recorido in enumerate(enumeracion):
    indice = recorido[0] # Indica que este valor ira primero
    valor = recorido [1] # Indicacion de que este va despues 
    print(f"El indice es {indice} y su valor es {valor}")

# (else) Esto es para indicar que el bucle ya termino 

for  anima in enumerate(animales):
    index = anima[0]
    cantida = anima[1]
    print(f"El numero es: {index} y el animal es: {cantida}")
else:
    print("Este es el final del Bucle")

# --------- En diccionario  --------


diccionario = {
    "nombre" : "Oscar",
    "Apellido" :"Romero",
    "Edad" : 20
}

# () Para un las claves es usar..

for i in diccionario:
    print(f"Y las claves son : {i}")


# (.items) Para leer el contenido de un (Diccionario)
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
     
    print(f"El valor de dato es {key} y eso significa {value} ")




verduleria = ["Durazno","Manzana","Papaya","Limon","Melon"]
 
# (continue) Para saltar un dato que no quieras
for i in verduleria:
    if i == "Papaya":
        continue 
    print(f"Las frutas seran : {i}")

# (breack) Detenr el bucle 

for i in verduleria:
    if i == "Manzana":
        break
    print("hubo un error en el codigo:") 


# Recorer una cadena de (texto)
word = "Romero"
for i in word:
    print(i)

# (for en una linea de codigo)
listado = [x*2 for x in enumeracion]
print(f"""La lista de numeros {enumeracion} 
        Y despues x 2 son : {listado}""")