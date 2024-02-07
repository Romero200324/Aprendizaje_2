# Concpetos de la creacionde ---(funciones integradas)---:

# (round) Agregacion de la cantida de decimales que le pidamos.
numero = round(23.3233,3)
print(numero)

# (bool) Simpres sera falso y le pasamos valores vaios o null
valores = bool("")
print(valores)

# (all) Para saber si tiene datos las listas (Treu)
comprecion = all("oscar")
print(comprecion)


# --------------(creacion de funciones)------------------

# (def) Asi de claramos una funcion propia 
def saludo():

    nombre = input("Dime tu nombre: ")
    genero = input("Dime que tipo de genero eres: ")
    print(f"Hola como estas {nombre} ?")

    genero = genero.lower()
    if genero == "femenino":
        print(f"Tu eres una mujer")
    elif genero == "masculino":
        print(f"Tu eres un Hombre")
    else:
        print("Eres un Elle...?")


saludo()

# (def) Con parametros 

def fecha_de_nacimineto (dia,mes,año):
    print(f"Tu fecha de nacimiento es : Día {dia} Mes {mes} y Año es {año}")

fecha_de_nacimineto(13,6,2003)


# Generador de IP: (Contreseña)
def crear_contraeña_random (num):
    chars = "abscjsjsjsd"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
# Retornación de valores.

    return (contraseña)
    
valor = crear_contraeña_random(34)
print(f"Tu contraseña es : {valor}")

    
# (*valor) De muchos parametros lo conbierte a uno
 
def restas(*numeros):
    sumacion = sum(numeros)
    return(sumacion)

print(restas(10,20,10,10,50))

# (*args) Para agregacion de otro parametro antes




def valor_de_suma (nombre_usuario,*numeracion):
    
    nombre_usuario = input("Dime tu nombre: ")    
    parametros = sum(numeracion)
    combinacion = print(f"Hola {nombre_usuario} la suma de tu listado es: {parametros}")
    return(combinacion)


valor_de_suma (" ", 12,34,45)

#(Relleno de datos) Otra forma de trabajar..

def sumacion_total (numeros):
    return sum([*numeros])

resultado = sumacion_total ([23,23,23,4])
print(f"El resultado de numercion es la siguientes: {resultado}")  
