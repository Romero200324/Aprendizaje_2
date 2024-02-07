# Crecion de ejercicios para el modulo de clases 

#1 Crecion de una clase que le pida al usuario un valor y lo multiplique por un dato random
class PeticionDeValor ():
    import random as rn
    valor = 4 #input("Ingrese un valor númerico: ")
    numeros_random = rn.randrange(11)

    operacion_de_valores = int(valor) * numeros_random

# Resultado Final.
resultado_final = PeticionDeValor.operacion_de_valores
random = PeticionDeValor.numeros_random
print(f"El número con el que fue multiplicado fue {random} y el resultado fue: {resultado_final}")    

print("""
________________________________________________
Ejercicio 2 
________________________________________________
""".upper())

#2 Clasificacion de articulos por orden de como fueron entregados 
# Teniendo como ejemplo que los pantalones furon primero depues fueron las camisas despues tenis y por ultimo las gorras
# Pero las prendas fueron entragas en diferentes horas del día y orden de llegada.

class clasificacion_de_prendas:
     
     # Recuerda siempre colocar bien el (__init__)
    def __init__(self,pantalones,camisas,tenis,gorras):
        self.articulo_1 = pantalones + " Pantalones"
        self.articulo_2 = camisas + " Camisas"
        self.articulo_3 = tenis + " tenis"
        self.articulo_4 = gorras + " gorras"

orden_corresponiente = clasificacion_de_prendas("12","12","34","34")
print(f"En el lugar se encontraron la cantida de : {orden_corresponiente.articulo_3}")





#3