peticion_de_valores = int(input("Ingres numeros para sumarlos: "))

def opercion (*peticion_de_valores):
    operacion_matematica = sum(peticion_de_valores)
    return(operacion_matematica)

resultado = opercion(peticion_de_valores)
print(f"El valor es : {resultado}")
