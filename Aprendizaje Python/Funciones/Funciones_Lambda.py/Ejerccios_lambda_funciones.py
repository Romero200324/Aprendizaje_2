# Apartado de ejercicios con funcines Lambda
def nombre (valor):
    nombre = valor.upper()
    return nombre

# (lambda) Creaion de una funion corta y simple
print(nombre("(lambda) Creaion de una funion corta y simple"))


#1  Crea con una función lambda,
# una calculadora de áreas de círculo

r =  float(input("Por favor introdusca el valor del radio del circulo: "))
pi = float(input("introduce el valor de PI en un circulos : "))

area_de_circulo = lambda : pi * r * r 
# Circulo: r = 23 pi = 3.1415
print(f"Area de circulo es :{area_de_circulo()} cm2")



#2

#3