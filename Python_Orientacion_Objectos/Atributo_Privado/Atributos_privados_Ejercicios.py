# (_contraseña) Ejercicios de atributos privados
class Mi_privacidad:
    def __init__(self):
        self._contraseña = "123456"

obtecion_de_contraseña = Mi_privacidad()

if obtecion_de_contraseña._contraseña == "123456":
            print(f"Obtecion de contraseña: {obtecion_de_contraseña._contraseña} ")

# (__oculto) Contrseña muy privada 
class Contraseña_oculta:
       def __init__(self):
              self.__oculto = "Llave de haceso a codigo fuente"

oculto_privado = Contraseña_oculta()
print(oculto_privado)



# Mestodos privados 
class valor():
       
    def __valor_resultado(self):
       print("Este valor es muy privado")


# Metodo un poco privado
class Oculto_privado():
      def _oculto_privado(self):
            self.no_ver_este_valor = "PolloPicante.200303" 


valor_oculto = Oculto_privado()
print(f"Valor oculto {Oculto_privado._oculto_privado()}")


