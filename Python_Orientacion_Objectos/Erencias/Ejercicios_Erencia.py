# Ejercios de (Herencia de clases)

#1 Aunto movil y sus propiedades de clases...

class Automovil():
    def __init__(self,color,ruedas,marca,modelo):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo

Auto_1 = Automovil("Rojo","Cromadas","Audi","Convertible")
print(f"El color de auto que sircula son: {Auto_1.color} ")


class Dia_de_no_circula(Automovil):
    def __init__(self,color,ruedas,marca,modelo,dia,mes,año):
        super().__init__(color,ruedas,marca,modelo)

        self.dia_circulacion = dia
        self.mes_circulacion = mes
        self.año_circulacion = año
    
    def aviso(self):
        print(f"Si usted pasa con su auto {self.marca} y modelo {self.marca}\n cera detenido")

Mes_de_viculacion = Dia_de_no_circula("Verdes","Cromadas","Ferrari","Ferrari 2023",13,6,2003)
print(f"El color de auto que sircula son: {Mes_de_viculacion.color}")

class Automoviles_sin_circulacion(Automovil):
    def __init__(self,color,ruedas,marca,modelo,advertencia,Nopasa):
     super(). __init__(color,ruedas,marca,modelo)

     self.advertanci = advertencia
     self.no_circula = Nopasa

no_sircula = Automoviles_sin_circulacion("Azul","Circulo","Toyota","Ligero","Usted no puede sircular","Multa de valor de $10,000")
print(no_sircula.no_circula)

# :\:\:\:\:\:\: Me quede en el video (1:00:11) :/:/:/:/:/:/:/:  




#2 Elaboracion de diversoso factores de los cuales son de un traporte

class Trasporte ():
    print("Aglomeracion de gente...")
    def __init__(self,estado,ruta,distacia,horario,consumo_de_gasolina,precios):
        
        self.estados = estado
        self.ruta = ruta
        self.kilometrage = distacia
        self.hora = horario
        self.gasolina = consumo_de_gasolina
        self.dinero = precios

ruta_1 = Trasporte("Publa","Ruta 11","12 km", "12:30 pm","3 Litros","$13")
print(ruta_1.ruta)


class Mexico (Trasporte):
    def __init__(self, estado, ruta, distacia, horario, consumo_de_gasolina, precios,terminal,estodo_de_terminal):
        super().__init__(estado, ruta, distacia, horario, consumo_de_gasolina, precios)

        self.ternimal = terminal
        self.termianl_del_estado = estodo_de_terminal

Autobus_de_estado = Mexico("Guadalajara","Federal Guadalajara - Puebla","250 km","00:00 am a 5:00 pm","25L","$1500","Puebla","Puebla-Puebla")
print(Autobus_de_estado.ruta)

#3