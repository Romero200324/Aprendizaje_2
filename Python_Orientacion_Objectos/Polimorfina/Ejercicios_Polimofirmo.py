# UN MISMO DATO DIFERENRES RESULTADO...

# Ejemplo 1 : Creacion de datos de una maquina tequilera...

class Tekila ():
    def __init__ (self, Ubicacion, Ventas, Producto,):
        
        self.ubicacion = Ubicacion
        self.ventas = Ventas
        self.produccion = Producto


class Puebla (Tekila):
    def __init__ (self,produccion_de_Octubre, ganacias, perdidas, Ubicacion, Ventas, Producto):
        Tekila.__init__(self,Ubicacion, Ventas, Producto)

       
        self.produccion = produccion_de_Octubre
        self.ganacias = ganacias
        self.perdidas = perdidas


class Mexico (Tekila):
    def __init__(self, ingresos, perdidas, daños, ):
        Puebla.__init__(self,valor)
        self.ingresos = ingresos
        self.perdidas = perdidas
        self.daños = daños 


def resumen_de_ventas (self):
    print(f"Las ventas estan de la siguite forma")



print()


        
        



        