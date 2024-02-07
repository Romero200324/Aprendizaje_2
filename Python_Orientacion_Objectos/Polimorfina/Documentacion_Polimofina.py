# SIGNIFICADO : Dar una mesaje y tener diferentes resultados....

class Gato():
    def sonido (self):
        print("Miau")
class Perro():
    def sonido (self):
        print("Guap")

def hacer_Sonido_animal (animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_Sonido_animal(gato)
print(perro.sonido())


# POLIMORFINO DE SOBRE CARGA : Cuando iniciamos con un valor y despues se aumenta...

# Ejercicios -- De explicacion -- 
class Empleado():

    def __init__(self):
        print("Hola bienvenido, como estas hoy ?")
    
    def __init__ (nombre,Edad,):
        print("La edad del empleado es: ....")

    def __init__ (nombre, Edad, Vivienda):
        print("El lugar en donde vive es en la parte de : ")

persona_1 = Empleado(20,"Puebla")

print (persona_1)

# OTRA FORMA DE VER EL POLIMORFISMO EN SU MINIMA EXPRECION ...

def recorrer (elementos):
    for item in elementos:
        print(f"El elemento actual : {item}")

lista = [1,2,3,4,5,6]
lista2 = ["Oscar","Romero","Romero"]


print(recorrer(lista2))

# UN ENLACE ESTATICO : Un dato que 

class Puebla ():
    
    # Declaracion de dato (ENLACE ESTATICO)
    @staticmethod
    def __init__(self):
        print("Explicacion de texto...")

# DUCK TYPING 

