# Ejercicios de herencias mutiple 


# 1 Cualidadades de las aves y las herencias que tiene ellos:

class Aves():
    def __init__(self,volar,gusanos,oviparos,pico):

        self.volar = volar
        self.comida = gusanos
        self.nacimiento = oviparos
        self.pico = pico


class Pato():
    def __init__(self,coloridos,migracion,temporadas,inicio,final): 

        self.colores = coloridos
        self.migracion = migracion
        self.temporada_pato = temporadas
        self.inicio = inicio
        self.final = final

    def notas(self):
        return f'Los pato son de color {self.colores} y ellos emigran a {self.migracion} en el mes de {self.inicio} y termina el mes de {self.final}'


class Paloma ():
    def __init__(self,semillas,lugar_encontrar,colores,usos_de_paloma):

        self.comida = semillas
        self.ubicacion = lugar_encontrar
        self.colores = colores
        self.tipos_de_palomas = usos_de_paloma


class Aves_tipos (Aves,Pato):
    def __init__(self,volar,gusanos,oviparos,pico,coloridos,migracion,temporadas,inicio,final,habla,garas):

        Aves.__init__(self,volar, gusanos, oviparos,pico)
        Pato.__init__(self,coloridos,migracion,temporadas,inicio,final)
        self.habla = habla
        self.gerras = garas

    def Varaciones(self):
        # (super()) Nos retorna los atributos que estan desde las clase padre... 
        print (f'{super().notas()}' )


ave_1 = Aves_tipos("20km","Alpiste","Huevo","Puntiagudo","verde","Mexico","5 meses","Enero","Mayo","Español","5cm")
ave_1.Varaciones()



# 2 Procediento para hacer galletas de (Chocolate, Pasas y Menta)

class Galletas ():
    def __init__(self,harina,maisena,leche,huevo,horno):

        self.harina = harina
        self.maisena = maisena
        self.leche = leche
        self.huevo = huevo
        self.horno = horno

    def procedimento (self):
        return f''' En la preparacion de las galletas es: 
        {self.harina} de harina 
        {self.maisena} de maisena
        {self.leche} de leche
        {self.huevo} de huevo
        {self.chocolate} de chocolate
        {self.menta} de menta
        {self.horno} para la prepacion  '''
    
class Cholate ():
    def __init__(self,chocolate,honeacion):

        self.chocolate = chocolate
        self.horneacion = honeacion

class Menta ():
    def __init__(self,menta,cocido):

        self.menta = menta
        self.hroneados = cocido

class Galletas_de_Menta (Galletas,Cholate,Menta):
    def __init__(self,harina,maisena,leche,huevo,horno,chocolate,horneacion,menta,hroneados):

        Galletas.__init__(self,harina,maisena,leche,huevo,horno)
        Cholate.__init__(self,chocolate,horneacion)
        Menta.__init__(self,menta,hroneados)


   
    def Reseta_GCM(self):
        print (  f'{super().procedimento()}')


Preparacion_GCM = Galletas_de_Menta("2k","25 mg","1L","3 piezas","45 minutos","25 gramos","r","12 gramos","t")

Preparacion_GCM.Reseta_GCM()






#