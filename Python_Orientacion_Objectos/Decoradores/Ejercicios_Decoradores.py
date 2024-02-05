# Ejercicio 1 (Decoradores)

# Cambio de nombre del usuario, pero si la contraseña no es correcta
# No lo podra hacer el cambio.
# print("Quieres cambiar tu nombre de usuario? ")
# class operacion_Camabio():
    
#     def cambio_de_nombre (cambio_de_nombre):
#             def esperacion():
#                 yes_o_no = input("Escriba la palbra si ó no: ".upper())
#                 if yes_o_no == "SI":
#                     print("En un moemnto podra ingrsar su nuevo nombre:  ")
#                 elif yes_o_no == input("NO"):
#                     print("Regrese a la pagina Inicial ")
#                 else:
#                     print("lo siento pero no eligio ninguna opcion")
#         # SEGUNDA PARTE DEL EJECICIIOS (decoracion)
#                 cambio_de_nombre()
#             return esperacion
#     # Pero es para ternimar un ciclo whithe ó for Utlizar (BRECK¡)
#     @cambio_de_nombre
#     def operaciones_ejcucion():
#         print(input(f"Escriba su nuevo nombre de usuario: "))
#     print(f"Tú nuevo nombre se usuario es: {super().esperacion()} ")
                


# # 2 Ejercicios
# # creacino de cambio de una valor (Pero) CON FUNCIONES PRIVADAS..

# class New_Pasword:

#     def __init__ (self,nombre_usuario,pasword):
#         # Valores privados..
#         self.nombre_usuario = "Romero_230"
#         self.pasword = "Romero_23"

#         @new_password

#         def implementacio_contraseña (New_Pasword):
#              print("La contraseña se esta cambiando.")
        
#         return(implementacio_contraseña)
        
#         def imprecion_de_valores(new_password,New_Pasword):
#              print(f"Lista la contraseña fue cambiada: {imprecion_de_valores}")


# # 3 Ejercicios

 # Decoracion de con operaciones matematicas...

def operaciones_mate(funt):
     def obciones(num_1,num_2):
         print( f"La suma de los numeros de {num_1} y {num_2}")

         return funt(num_1, num_2)
     return obciones


@operaciones_mate
def sum_nums(num_1, num_2):
     return num_1 + num_2 

print(sum_nums(23,2))


# 4 (EJERCICIO)
# Multiplicaion de numeros random 


import random

def ramndon(mate):
# Mostrando los datos (Random)
    def multiplicacion_datos(num_ram_1, num_ram_2):
        num_ram_1 = random.randrange(0, 11)
        num_ram_2 = random.randrange(0, 11)
    valor = print(f"los numeros {num_ram_1} y {num_ram_2} son random.")
    return valor


@ramndon
def multiplicacion_valores(num_ram_1, num_ram_2):
  return num_ram_1 * num_ram_2

print(multiplicacion_valores)

