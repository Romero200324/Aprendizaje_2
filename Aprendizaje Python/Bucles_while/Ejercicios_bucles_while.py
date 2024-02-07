# Secion de ejercicios con el while 

# (While) Simpre que sea verdadero este codigo se ejecutara 

#1 Asignacion de fechas de cumpleaños 
años = 2000

while años < 2003:
    años+= 1
    print(f"Los años que he cumplido son : {años}")



# Acceso a un pagina para mayores de 18 años 

años_de_la_persona = 1

while años_de_la_persona <= 18:
    años_de_la_persona += 1
    
    if años_de_la_persona >= 18:
      print(f"Lista ya cumplsite los años suficientes : {años_de_la_persona} ")

    elif años_de_la_persona <= 18:
        print(f"Eres muy jonven aun {años_de_la_persona}") 


#2 Escribir un programa que pida al usuario un número 
# entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. 

n = int(input("Escriba un numero "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")










#3