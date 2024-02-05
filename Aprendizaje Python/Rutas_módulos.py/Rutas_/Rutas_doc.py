# Importacion de mudulos en las extenciones...

# Asignaicon de avatar (Ramdon)
import random

def avatar_usuario ():
    numeros_random = random.randrange(0, 5)
    avatar_selccionales = ("Pajaro","Conejo","Gallina","Pato","Gato")
    
    avatar_final_del_usuario = avatar_selccionales[numeros_random]
    print(f"El avartar asignado para ti es: {avatar_final_del_usuario}")

