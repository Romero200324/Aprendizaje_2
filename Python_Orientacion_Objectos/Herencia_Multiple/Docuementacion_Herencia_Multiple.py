# Docuemetacion de herencia multiple para apreder 

class Juegos ():
    def __init__(self,nombre,jugadore,reglas,tiempo_de_partida):

        self.nombre_del_juego = nombre
        self.jugadores = jugadore
        self.reglas = reglas
        self.tiempo = tiempo_de_partida



class Video ():
    def __init__(self,pixeles,color,sonido):
        
        self.pixeles = pixeles
        self.colores = color
        self.sonido = sonido


    def video_imagen(self):
        return (f"Calidad de imagen de calida de pixeles es: {self.pixeles} y de sonido es {self.sonido} y el videoJuego es {self.nombre_del_juego}")



class videoJuegos (Juegos,Video):
    def __init__(self,nombre,jugadore,reglas,tiempo_de_partida,pixeles,color,sonido,cosola,generacion,megapixeles):
        Juegos.__init__(self,nombre,jugadore,reglas,tiempo_de_partida)
        Video.__init__(self,pixeles,color,sonido)

        self.consola_de_videojuego = cosola
        self.generacion_de_consola = generacion
        self.calidad = megapixeles

     
    def valor(self):
        # (super()) Nos retorna los atributos que estan desde las primeros valores. 
        print (f'{super().video_imagen()}' )

Consola_1 = videoJuegos("Super Smasll Bros","5 personas","No perder vidas","5 minutos","250 px","Muchos colores","Banda Sonara","Nintendo 64","Primera Generacion","1T")
Consola_1.valor()


# (issubclass) Para saber si la clase es una sub clase
herencia = issubclass(videoJuegos,Video)

if herencia == True:
    print ("Esta es tu clase es una sub clase...")

elif herencia == False:
    print("Esta no es una sub clase...")

else:
    print("El valor que ingresaste un pertinece esto modulo")