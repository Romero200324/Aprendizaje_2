# 1 ejercios de Setters y implemetacion de nuevo elementos

# Hacer el cambio de nombres de los usuarios...

class nombre_de_usuario():
    def __init__(self, nombre,contraseña):
        self._nobre = nombre
        self._contraseña = contraseña

    def get_datos (self):
        return self._contraseña


# Implementacion de un nuevo dato 

    def set_implemetacion_nombre (self, nuevo_nombre):
        self.nombre = nuevo_nombre
# Imprecion del dato final

cambio_de_nombre = nombre_de_usuario("Oscar Romero Romero","Romeero")

operacion_de_datos = cambio_de_nombre.get_datos()
print(operacion_de_datos)

nuevo_nombre = cambio_de_nombre.set_implemetacion_nombre("Pepe Agilar")

# Variables publicas..

imprecion_de_datos = cambio_de_nombre.get_datos()
print(f"El cambio de la comtraseña es:{operacion_de_datos} ")