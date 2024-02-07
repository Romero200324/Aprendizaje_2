# Toda la documentacion de los datos...

# Inicializacion de una clase
class Celulares():
    
    # Creacion de una  instancia de la clase 
    marca_1 = "Apple"
    modelo = "XP"
    camara = "39PX"

celular_1 = Celulares.marca_1 #Ejecucion clase
print(celular_1)



# Otra formas más optima de hacer las cosas 
print("""
------------------------------------------------------------
Otra forma de hacer que el trabajo sea menos y más rapido
------------------------------------------------------------
""".upper())

class Fabricaion_celular:
    # (self) Es una funcion detro de la propia classe 
    def __init__(self,marca,modelo,color,camara):
        self.marca_1 = marca
        self.modelo_1 = modelo
        self.color_1 = color
        self.camara_1 = camara


# Impreicion del contenido de la classe en cuestion 
componentes_modelo_1 = Fabricaion_celular("Apple","14 P","Morado Bajo","50px")
componentes_modelo_2 = Fabricaion_celular("Cricket","Modelo 11","Verde inteso","70MP")

# Componente en especifico 
print(componentes_modelo_2.camara_1)