# Toda la documentacion sobre los metodos asi como explicaciones...

class modelos_de_celular:
    def __init__(self,modelo,generacion,camara,):
        self.modelo = modelo
        self.generacion_de_celular = generacion
        self.pixiles_de_la_camara = camara 

        #   Metodos para python
    def llamada_en_progreso (self):
        print(f"Usted esta llamando desde un celular {self.modelo}")

    def cortar_llamada (self):
        print(f"Colgo la llamada desde un celular {self.modelo} modelo {self.generacion_de_celular}")

celular_1 = modelos_de_celular("Apple","Quinta generación","59px")
celular_2 = modelos_de_celular("Sansum","Decima generaion","89px")

celular_1.llamada_en_progreso()
celular_2.cortar_llamada()