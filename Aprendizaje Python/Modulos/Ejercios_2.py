# Importacion de funciones  otros

# 1 Creacion de funcion de nombre de (Perros)
#print("------------------ Ejemplo 1_1 -----------------")

import random 

def nombres_de_canes ():
    numeros_random = random.randrange(0, 11)
    nombres_canino = ["Rocky","Brian","Reina","Nemo","Golfo","Bolt","Nala","Hachiko","Truman","Simba","Lassie","Pongo"]

    nombre_final = (nombres_canino[numeros_random])
    print(f"El nombre de tu perro ideal sera: {nombre_final}")



import time

def hoy ():
    dia_hoy = time.strftime("%H:%M:%S")
    print(f"la hora es: {dia_hoy}")


import random 

def musica_de_eleccion ():


        valor = 10
        while valor < 200:
                valor+= 1
                #elecicion
                gusto_musical = input("¿Cuál es su género musical?: ")
                listado_de_canciones = ("rock","cumbia","bolero","reggae","tango","salsa")
                #random
                musica_random = random.randrange(0,10)
                # Time
                hora_musica = time.strftime("%H:%M:%S")

                if gusto_musical.lower() == "rock":
                    lista_cancion = [
                "Por la boca vive el pez. Fito y Fitipaldis",
                "So payaso. Extremoduro.",
                "Rock & Roll Star (feat. Sabino Méndez) - Bec 05.",
                "Agradecido - Directo 99. Rosendo.",
                "El roce de tu cuerpo. Platero Y Tu.",
                "La posada de los muertos. Mägo de Oz.",
                "Víctima. Barricada.",
                "La cabecita loca. Rulo y la contrabanda.",
                "3+1. Panda",
                "La rosa de los vientos. Mägo de Oz",
                ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")
                
                elif gusto_musical.lower() == "cumbia":
                    lista_cancion = [
                        "La cumbia de los vaqueros(Bukano)",
                        "La cumbia de los zombies(Bukano)",
                        "Suelta el listón de tu pelo(Angeles Azules)",
                        "El Afilador (Grupo Carabo)",
                        "Te Digo Vete (Los Askis)",
                        "Conga y timbal (Yaguaru)",
                        "Amor Carnal (Chon Arauza y La Furia Colombiana)",
                        "Todo Me Gusta de Ti (Aaron y Su Grupo Ilusion)",
                        "El Poder de Tu Amor (Grupo Perla Colombiana)",
                        "Mi Cafetal (Tropa Vallenata)"
                        ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")
                            
                elif gusto_musical.lower() == "bolero":
                    lista_cancion = [
                        "Bésame mucho - Consuelo Velázquez",
                        "Contigo en la distancia - César Portillo de la Luz",
                        "Sabor a mí - Álvaro Carrillo",
                        "Historia de un amor - Carlos Eleta Almarán",
                        "Perfidia - Alberto Domínguez",
                        "Si nos dejan - José Alfredo Jiménez",
                        "La barca - Roberto Cantoral",
                        "Quizás, quizás, quizás - Osvaldo Farrés",
                        "Somos novios - Armando Manzanero",
                        "Esta tarde vi llover - Armando Manzanero"
                    ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")

                elif gusto_musical.lower() == "reggae":
                    lista_cancion = [
                    
                        "- I Shot The Sheriff – Bob Marley & the Wailers. ...",
                        "- Many Rivers To Cross – Jimmy Cliff. ...",
                        "- I Can See Clearly Now – Johnny Nash. ...",
                        "- You Can Get It If You Really Want – Jimmy Cliff. ...",
                        "- Israelites – Desmond Dekker & the Aces. ...",
                        "- No Woman, No Cry – Bob Marley & the Wailers.",
                        "Is This Love",
                        "No Woman No Cry",
                        "One love",
                        "King Without a Crown"
                        
                    ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")
                elif gusto_musical.lower() == "tango":
                    lista_cancion = [

                        "Carlos de Gardel – Mi Buenos Aires Querido ...",
                        "Edmundo Rivero – Cafetín de Buenos Aires ...",
                        "Carlos de Gardel – Por una cabeza ...",
                        "Cesaria Evoria – Besame mucho ...",
                        "Julieta Venegas y Bajo Fondo – Pa’ Bailar",
                        "A media luz",
                        "Afiches",
                        "Angustia",
                        "Por una cabeza",
                        "Mi Buenos Aires querido"
                        
                    ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")
                elif gusto_musical.lower() == "salsa":
                    lista_cancion = [

                        "Aquel lugar - Adolescent's Orquesta",
                        "Pedro Navaja - Rubén Blades",
                        "Vivir mi vida - Marc Anthony",
                        "Llorarás - Óscar D'León",
                        "Quítate tú - Fania All-Stars",
                        "La murga - Willie Colón",
                        "Aquel lugar - Adolescent's Orquesta",
                        "Periódico de ayer - Héctor Lavoe",
                        "El gran varón - Willie Colón y Héctor Lavoe",
                        "Salsa y control - La 33"
                    ]
                    print (f"Son las ({hora_musica}) y es momento de escuchar: {lista_cancion[musica_random]}")

                elif gusto_musical.lower() == "ver lista":
                     print(listado_de_canciones)

                elif gusto_musical.lower() == "terminar":
                    print("Espero que las canciones hayan sido de su gusto...")
                    break
                    

                else:
                    print("""Estoy seguro de que el género en el que ingresaste no está registrado., 
                                     intente con otro genero...""")


#def contraseña_del_usuario ():
 #   print("""La contraseña debe contern al menos 6 caracteres
 #                       y un maximo de 12 """)
 #   contraseña_usuario = input("Ingrese la contraseña: ")

 #   num_entero = str(contraseña_usuario)
 #   operacion_de_contraseña = int(num_entero[0])

    # Calculacion de para contar letrar dentro de un strg()
 #   for i in operacion_de_contraseña:
 #        index = 1[0]   

            
#contraseña_del_usuario()