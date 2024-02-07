# Documentacion de los Atributos Privados 

class MiClass:
    def __init__(self):
        self._atributo_privado = "Contraseña"

objectos = MiClass()
print(objectos._atributo_privado)

# Atributos mas privado..

class Llave_de_acceso:
    def __init__(self):
        self.__no_acceder = "PolloPicate200034"

objecto_privado = Llave_de_acceso()
print(objecto_privado.__no_acceder)

if objecto_privado == False:
    print("No accedas a este archivo...")