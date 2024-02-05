# Metodologia del un Diccionario seran los valores...

libros_leidos_2022 = {
    'Autor' : "Jk Rovin",
    'Nombre_del_libro':"Harry Potter",
    'Tipo_de_lectura' : "Aventura, Fantacia",
    'Tiempo_tomado': "Enero - Junio",
    'Resumen_del_libro': "Es una aventua entretenida por muchos motiovos de los cuales fueron por parte de que la trama era emocionate por los dragones..."
}

# (Keys) Muestra los nombres de un diccionario
print("(Keys) Muestra los nombres de un diccionario".upper())

interaciones = libros_leidos_2022.keys()
print(interaciones)



#(get) Buscar el dato  de tú interes, (interacion que buscas)
print("(get) Buscar el dato  de tú interes, interacion que buscas".upper())

un_datos_especifico = libros_leidos_2022.get("Autor")
print(f"El autor del libro es : {un_datos_especifico}")


#(pop) Eliminacion de un elemento en especifico
print("(pop) Eliminacion de un elemento en especifico".upper())

libros_leidos_2022.pop("Resumen_del_libro")
print(f"Los datos pasaron por un filtrado: {libros_leidos_2022}")


#(intens) Agrupacion de datos en grupos (----,----)
print("(intens) Agrupacion de datos en grupos (----,----)")

separacion_de_datos = libros_leidos_2022.items()
print(f"Los datos ansido separados por grupos: {separacion_de_datos}")


#(clear) Elimina todo el deccionario 
print("(clear) Elimina todo el deccionario".upper())

eliminacion_del_diccionario = libros_leidos_2022.clear()

if eliminacion_del_diccionario != {}:
    print(f"Los datos fueron elimiandos correctamente: {eliminacion_del_diccionario}")
else:
    print(f"Lo siento pero creo que cometio un error en el codigo: {eliminacion_del_diccionario}")

