# Documentacion de Decoradores 

# (funtion) Implementacion de un nuevo elemento...
def codigo_decorado (funcion):
    def funcion_modificada():
        print("El ejercicio fue expresado correctamente")

        # Decoracion del codigo...
        
        print(f"La accion que implento fue: ")
        funcion()
    return funcion_modificada 


# (Decorador): Aplicada de manera más largo


# valor_resultado = codigo_de_corado(operacion) 
# valor_resultado()

# (@codigo_decorado): Aplicada de la menera más conpacta
@codigo_decorado

def operacion(): 
     print("Exitosa !!")
     

# IMPLEMENTACION DE DECORACION EN UNA VARIBLE PRIVADAS
# class valores_privados():

#     def __init__(self,nombre):
#         self.nombre = "Osca Romero"

#     def valor_del_dato(self,valor):
#         self.valor = "Romero"

#         return valores_privados()
    
# print(f"El resultado fue: {valores_privados.valor_del_dato}")

class valores_privados():
    def __init__(self, nombre):
        self.nombre = nombre

    def valor_del_dato(self, valor):
        self.valor = valor
        return self

instancia = valores_privados("Osca Romero")
print(f"El resultado fue: {instancia.valor_del_dato('Romero').valor}")


# Implementacion de propiedades 
# Valores ocultos es importante (CLASS)

class valores_ocultos:
    def __init__ (self,valor,significado):
        self.__valor = valor
        self._significado = significado

    @valores_ocultos
    def resultados_valores(self):
        return self.__valor

valor_ocul = valores_ocultos("Romero","Denominacion")
resultados = valor_ocul.resultados_valores
print(resultados)
