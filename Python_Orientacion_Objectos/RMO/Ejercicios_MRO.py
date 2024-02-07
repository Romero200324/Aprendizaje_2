# Ejerccios de los todos los terminos de RMO


# 1 limpieza de datoa y clasificacion 
class D ():
    def hablar (self):
     print("Hola de D")

class B (D):
   def hablar (self):
      print("Hola de B")

class J(B,D):
   def hablar (self):
      print("Hola de C")

class H (J,B):
   def hablar (self):
      print("Hola de H")

class P(H,J):
   def hablar (self):
      print("Hola de P")

class G (P,J):
   def hablar (self):
      print("Hola de G")

class N(P,H,J,B,D):
   def hablar (self):
      print("Hola de N")

valor = N()
valor.hablar()

# Ruta de ejecucion.. 
print(N.mro())




# Ejemplo 2 :

#  Crear un sistema para una escuela. En donde tendremos 2 clases (
# Personas: Nombre y Edad , Metodo: Nombre, Edad  
# Estudiantes:  (Persona), grado : Metodo : Grado del estudiante.

# Utilizar : (Super), (init), (Instancias)

class Persona():
   def __init__ (self,nombre,edad):
      self.nombre = nombre
      self.edad = edad


class Estudiante(Persona):
   def __init__(self,nombre, edad,grado):
    super(). __init__(nombre,edad)
    self.grado = grado


   def oracion (self):
      print("Binevenido")


persona_1 = Persona("oscar Romero", 20)
estudiante_1 = Estudiante("Romero", 20, "Segundo semestre de Universidad")

estudiante_1.oracion()


# Crear 3 clases ( Animal), (Manifero), (Ave) 
# ANIMAL : Comer 
# MANIFERO : "amamantar"  
# Aves "Volar"

# Cracion de la clase MURCIELAGO (amamantar , valora , comer )
# Jugar conls metodos para |super()|



class Animal() :
   def __init__ (self, comer):
      self.comer = comer 

class Manifero(Animal):
   def __init__ (self,amamantar):
      self.amamantar = amamantar

class Aves(Animal):
   def __init__ (self,volar):
      self.volar = volar 

class Murcielago(Manifero,Aves):
   def __init__(self,comer, amamantar, volar):
      Animal.__init__(self,comer)
      Manifero.__init__(self,amamantar)
      Aves.__init__(self,volar)

Animal_manifero = Murcielago("Pollo Frito","2 meses","1 Kilometro")


print(Animal_manifero.volar)