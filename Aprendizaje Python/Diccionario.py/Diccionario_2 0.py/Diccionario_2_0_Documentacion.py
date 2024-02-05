# Creacion de diccionario diferentes maneras


# (dict) Definicion de crear diccionario
diccionario = dict(nombre="Oscar",apellido ="Romero")
print(f"Primer valor del diccionario es : {diccionario}")



#(Frozenset) Congelar datos para unir otros datos en un mismo conjunto.
diccionario = {frozenset((["edad","20"])): "Programador"}
print(f"Segundo valor del diccionario es : {diccionario}")



#(dict.(fromkeys)) Creación de datos (bacios)
diccionario = dict.fromkeys(["nombre","apellido","hobit"])
print(f"Tercer valor del diccionario es: {diccionario}")
