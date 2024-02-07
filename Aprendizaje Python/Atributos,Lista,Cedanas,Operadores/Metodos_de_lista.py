#Metodos de listado

cumpla_años =  {
    'Oscar' : "13/09/2000",
    'Luca':"12/08/2000"

}
secuencia = ([ 23,23,32,1,5,80,6,4,34,4,5,45,4])
listado = list(["oscar","romero","romero"]) # (list) Este es el metodo más común
print(listado)

#len
contenido_de_una_lista = len(listado) # (len) Cuenta cuantos elementos tiene el "Array"
print(contenido_de_una_lista)

#append 
listado.append("20") # (append) Se agregara un nuevo elemento al "Array" en final
print(listado)

# insert
listado.insert(2,"power") # (insert) Colocar el nuevo elemento en una posición fija
print(listado)

# extend
listado.extend(["w","ua"]) # (extend) Agregar un Array a un Array 
print(listado)

# pop
listado.pop(3) # (pop) Eliminacion de valores en un listado.
print(listado)

# remove
listado.remove("oscar") #(romove) Nombrar el elemento que queres eliminar del Array.
print(listado)


# clear 
cumpla_años.clear() #Eliminación de toda la lista de elementos que hay dentro de ella 
if cumpla_años != True:
    print("Listo la lista ya se elimino")
else:
    print("No se pudo eliminar")    
print(f"Esto es lo quedo de las lista: {cumpla_años}") 


# sort 
secuencia.sort() # Acomoda los valores de forma acedente..
print(secuencia)


# sort.(reversed) 
secuencia.sort(reverse=True) # Acomoda los valores de forma decendente...
print(secuencia)

# reverse()
secuencia.reverse() # Le da la vuelta completa a un (Array)
print(secuencia)
