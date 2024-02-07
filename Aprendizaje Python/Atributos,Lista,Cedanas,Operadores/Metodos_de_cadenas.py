#Sección de cadenas 
nombre = "Oscar"
apellido = "Romero"
listado_numerico = (23432434324)
oracion = "Habia una vez un perro que se llamaba goma un día se rasco y se borro... "

# Terminologia para anidar codigo (Anidadores) 

print(dir(apellido)) #(dir): Muestra todos los atributos que puede tener.

print(nombre) #(type) Nos dice que tipo de dato es...
type(nombre)

mayusculas = nombre.upper() #(upper) Pasa todo el texto en mayusculas 
print(mayusculas)

minusculas = apellido.lower() #(lower) Para todo el texto a minusculas.
print(minusculas)

primer_letra_en_mayusculas = nombre.capitalize() # (capitalize) Coloca la primera letra en mayusculas.
print(primer_letra_en_mayusculas)

conteo_de_palabras = nombre.find("a") # (find) conteos de palabras en el texto
print (conteo_de_palabras)

lazamiento_de_ecepciones = nombre.index("s") # (index) Aparacion de un ecepcion y deteción del programa
print(lazamiento_de_ecepciones)

numeros_en_un_variable = listado_numerico.isnumeric() # (isnumeric) Inspeciona si la varible tiene numeros
print(numeros_en_un_variable)

solo_letras = nombre.isalpha() # (isalpha) Escribe letras de A a Z
print(solo_letras)


coincidencias = oracion.count("perro") # (count) De acuerdo a la similitud de la oración
print(f"El dato que busca es este : {coincidencias}")

#-------- Funcion ------------

conteo_de_caracteres = len(oracion) # (len) Cuenta cada palabra que tiene
print(conteo_de_caracteres)

empieza_con = oracion.startswith("Habia") #  (startswith) Inicio de una oracion inicia con...
print(empieza_con)

termina_con = oracion.endswith("borro") # (endswith) Termina con la (palabra,letra,oracion) de...
print(termina_con)

remplazamiento_cadenas = oracion.replace("borro","masco") # (replace) cuando encuentra una coincidencia se remplaza por otra de tu elección
print(remplazamiento_cadenas)




separacion_de_cadenas = oracion.split(" ") # (split) separa una (Oracion y texto).Se convierte en una lista, Tupla
print(separacion_de_cadenas)




