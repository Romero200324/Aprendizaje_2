# Hacer una propiedades en donde el dasarrollador no pueda accerder 
# En otras palabras hacar una un atributo "PRIVADO"...


# (self.__) ---> CONJUNTO MUY PRIVADO <---
class Contraseña ():
    def __init__(self):
            self.__satributo_privado = "Romero_20"

# (def__valor) ---> METODOS PRIVADOS <---
    def valor (self):
         print("La contraseña se decifro corectamente...")

mostrar_contraseña = Contraseña()
print(mostrar_contraseña.valor())



# (self._) ---> CONJUNTO PRIVADO <---
class Generador_contraseña ():
    def __init__(self):
        self._atributos_privado = "Valor"

objecto = Generador_contraseña  ()
print(objecto._atributos_privado)



# HACERDER A VALORES PRIVADAS DE LA SIGUIENTE FORMA..

class Valor_oculto ():
       
    def __init__ (self,password):
         # DATO OCULTO 
         self._password = password

    def get_password (self):
         return self._password
    
            # -- > LLAMADO A SET <--

    def set_password (self, new_password):
        self._password = new_password

    
password_1 = Valor_oculto("PolloPicante")

if password_1 == "PolloPicante":
     print("La operacion fue ejecutada correctamente...")

recuperacion_password = password_1.get_password()
print(recuperacion_password)




     