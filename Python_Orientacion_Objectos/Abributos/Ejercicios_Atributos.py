# Documentacion de los Atributos

class Celular:
        
        # (__init__) Inicializacion de primer instancia .
        # (self) Hace referencia al mismo clase.
        def __init__(self,marca,modelo,camara,color):
            self.valor_1 = marca
            self.valor_2 = modelo
            self.valor_3 = camara
            self.valor_4 = color
    
        
        # Todos los elmentos deben ser similares si no tira un error (Exepcion)

celular_1 = Celular("Apple", "15","59 MP","verde")
celular_2 = Celular("Sanmgun","Pro 23", "49 MP","Morado")

print(celular_2.valor_1)   


