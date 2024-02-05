#   Documentacion mas importante de RMO

# Herencias de propiedades ()

class A:
    def _hablar(self):
        print("Hola desde A")

# Funciones privadas () ó metodos privado
class B(A):
    def _hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class coreano (A):
    def hablar(self):
        print("Hola yo hablo coreano y japones")

class D(coreano,B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

# Ejecucion de la clase anterior ó cual quier clase.

B.hablar(d)


# (.mro) Mostrar toda la ruta ejecucción ...

print(D.mro())