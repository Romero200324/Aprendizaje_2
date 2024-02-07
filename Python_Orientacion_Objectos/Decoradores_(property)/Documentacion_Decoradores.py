# Documentacion de los documentos...

class Documento_regulado():
    def __init__(self,Documento,valores):
        self.documetacion = Documento
        self.atributos_valores = valores

    def get_valores_regulados(self):
        return self.atributos_valores 
    
nombre_del_documento = Documento_regulado("Seguirdad privadad", "Nombre de participantes")